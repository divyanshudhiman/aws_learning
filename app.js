(() => {
  const cfg = window.GUIDE_CONFIG || {};
  const storagePrefix = cfg.storagePrefix || "aws-ai-learning";
  const content = document.getElementById("markdown-content");
  const nav = document.getElementById("section-nav");
  const libraryToggle = document.getElementById("library-toggle");
  const searchInput = document.getElementById("search-input");
  const searchResults = document.getElementById("search-results");
  const menuToggle = document.getElementById("menu-toggle");
  const sidebar = document.getElementById("sidebar");
  const backdrop = document.getElementById("sidebar-backdrop");
  const progress = document.getElementById("reading-progress");
  const sectionCount = document.getElementById("section-count");
  const resumeButton = document.getElementById("resume-button");
  const readingKey = `${storagePrefix}-last-section`;
  const libraryOpenKey = `${storagePrefix}-library-open`;
  const groupsOpenKey = `${storagePrefix}-nav-groups`;

  let searchableBlocks = [];
  let activeNavLink = null;

  function slugify(value) {
    return value
      .toLowerCase()
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-|-$/g, "");
  }

  function readOpenGroups() {
    try {
      const raw = localStorage.getItem(groupsOpenKey);
      return raw ? JSON.parse(raw) : {};
    } catch (error) {
      return {};
    }
  }

  function writeOpenGroups(map) {
    try {
      localStorage.setItem(groupsOpenKey, JSON.stringify(map));
    } catch (error) {
      console.warn("Could not save nav group state.", error);
    }
  }

  function setGroupOpen(group, open) {
    group.classList.toggle("is-open", open);
    const toggle = group.querySelector(".nav-group-toggle");
    const panel = group.querySelector(".nav-group-panel");
    if (toggle) {
      toggle.setAttribute("aria-expanded", String(open));
    }
    if (panel) {
      panel.hidden = !open;
    }
  }

  function buildNavigation() {
    const headings = Array.from(content.querySelectorAll("h1, h2"));
    const usedIds = new Map();
    const fragment = document.createDocumentFragment();
    const savedGroups = readOpenGroups();
    let sectionTotal = 0;
    let currentGroup = null;
    let currentPanel = null;
    let openCount = 0;

    function ensureIds(heading, index) {
      const label = heading.textContent.trim();
      const baseId = slugify(label) || `section-${index + 1}`;
      const seen = usedIds.get(baseId) || 0;
      usedIds.set(baseId, seen + 1);
      heading.id = seen ? `${baseId}-${seen + 1}` : baseId;
      return label;
    }

    function startGroup(heading, label) {
      const group = document.createElement("div");
      group.className = "nav-group";
      group.dataset.groupId = heading.id;

      const toggle = document.createElement("button");
      toggle.type = "button";
      toggle.className = "nav-group-toggle";
      toggle.setAttribute("aria-controls", `nav-panel-${heading.id}`);
      toggle.setAttribute("aria-expanded", "false");

      const chevron = document.createElement("span");
      chevron.className = "nav-group-chevron";
      chevron.setAttribute("aria-hidden", "true");
      chevron.textContent = "▸";

      const title = document.createElement("span");
      title.className = "nav-group-title";
      title.textContent = label;

      toggle.append(chevron, title);

      const panel = document.createElement("div");
      panel.className = "nav-group-panel";
      panel.id = `nav-panel-${heading.id}`;
      panel.hidden = true;

      // First item always jumps to the Part heading itself.
      const partLink = document.createElement("a");
      partLink.className = "nav-link nav-group-heading";
      partLink.href = `#${heading.id}`;
      partLink.textContent = "Overview";
      partLink.title = `Go to ${label}`;
      partLink.addEventListener("click", closeNavigation);
      panel.append(partLink);

      group.append(toggle, panel);

      const preferOpen = savedGroups[heading.id];
      const shouldOpen = preferOpen === undefined ? openCount < 1 : Boolean(preferOpen);
      setGroupOpen(group, shouldOpen);
      if (shouldOpen) {
        openCount += 1;
      }

      toggle.addEventListener("click", (event) => {
        event.preventDefault();
        const nextOpen = !group.classList.contains("is-open");
        setGroupOpen(group, nextOpen);
        const map = readOpenGroups();
        map[heading.id] = nextOpen;
        writeOpenGroups(map);
      });

      fragment.append(group);
      currentGroup = group;
      currentPanel = panel;
    }

    headings.forEach((heading, index) => {
      const label = ensureIds(heading, index);

      if (heading.tagName === "H1") {
        sectionTotal += 1;
        startGroup(heading, label);
        return;
      }

      const link = document.createElement("a");
      link.className = "nav-link level-two";
      link.href = `#${heading.id}`;
      link.textContent = label;
      link.title = label;
      link.addEventListener("click", closeNavigation);

      if (currentPanel) {
        currentPanel.append(link);
      } else {
        fragment.append(link);
      }
    });

    nav.replaceChildren(fragment);
    sectionCount.textContent = String(sectionTotal);
    return headings;
  }

  function buildSearchIndex() {
    searchableBlocks = Array.from(content.querySelectorAll("h1, h2, h3, p, li, td, blockquote"))
      .map((element, index) => {
        if (!element.id) {
          element.id = `guide-item-${index + 1}`;
        }
        return {
          element,
          text: element.textContent.replace(/\s+/g, " ").trim(),
        };
      })
      .filter((entry) => entry.text.length > 0);
  }

  function findSectionTitle(element) {
    let current = element;
    while (current && current !== content) {
      if (/^H[1-3]$/.test(current.tagName)) {
        return current.textContent.trim();
      }
      current = current.previousElementSibling || current.parentElement;
    }
    return "Study guide";
  }

  function getSnippet(text, query) {
    const lowerText = text.toLowerCase();
    const lowerQuery = query.toLowerCase();
    const phraseIndex = lowerText.indexOf(lowerQuery);
    const index = phraseIndex >= 0
      ? phraseIndex
      : Math.min(...lowerQuery.split(" ").map((term) => lowerText.indexOf(term)));
    const start = Math.max(0, index - 70);
    const end = Math.min(text.length, index + query.length + 110);
    return `${start > 0 ? "…" : ""}${text.slice(start, end)}${end < text.length ? "…" : ""}`;
  }

  function runSearch() {
    const query = searchInput.value.trim().replace(/\s+/g, " ");
    searchResults.replaceChildren();

    if (query.length < 2) {
      searchResults.hidden = true;
      return;
    }

    const terms = query.toLowerCase().split(" ");
    const matches = searchableBlocks
      .filter((entry) => terms.every((term) => entry.text.toLowerCase().includes(term)))
      .slice(0, 8);

    if (matches.length === 0) {
      const empty = document.createElement("p");
      empty.className = "search-empty";
      empty.textContent = "No matches yet. Try a different keyword.";
      searchResults.append(empty);
    } else {
      matches.forEach(({ element, text }) => {
        const result = document.createElement("a");
        result.className = "search-result";
        result.href = `#${element.id}`;

        const title = document.createElement("strong");
        title.textContent = findSectionTitle(element);
        const snippet = document.createElement("span");
        snippet.textContent = getSnippet(text, query);
        result.append(title, snippet);
        result.addEventListener("click", () => {
          searchResults.hidden = true;
          searchInput.value = "";
        });
        searchResults.append(result);
      });
    }

    searchResults.hidden = false;
  }

  function updateActiveNavigation(headings) {
    const current = headings
      .filter((heading) => heading.getBoundingClientRect().top <= 130)
      .at(-1);

    if (!current) {
      return;
    }

    if (activeNavLink) {
      activeNavLink.classList.remove("active");
    }

    activeNavLink = nav.querySelector(`a[href="#${CSS.escape(current.id)}"]`);
    if (activeNavLink) {
      activeNavLink.classList.add("active");
      const group = activeNavLink.closest(".nav-group");
      if (group && !group.classList.contains("is-open")) {
        setGroupOpen(group, true);
        const map = readOpenGroups();
        map[group.dataset.groupId] = true;
        writeOpenGroups(map);
      }
    }

    try {
      localStorage.setItem(readingKey, current.id);
    } catch (error) {
      console.warn("Could not save reading position.", error);
    }
  }

  function updateProgress() {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const percent = scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0;
    progress.style.width = `${Math.min(100, Math.max(0, percent))}%`;
  }

  function closeNavigation() {
    sidebar.classList.remove("is-open");
    backdrop.hidden = true;
    menuToggle.setAttribute("aria-expanded", "false");
  }

  function showLoadError(message) {
    const wrapper = document.createElement("div");
    wrapper.className = "error-state";
    const title = document.createElement("strong");
    title.textContent = "Your study guide couldn’t be loaded.";
    const detail = document.createElement("p");
    detail.textContent = message;
    wrapper.append(title, detail);
    content.replaceChildren(wrapper);
  }

  function getSavedSection() {
    try {
      return localStorage.getItem(readingKey);
    } catch (error) {
      console.warn("Could not restore reading position.", error);
      return null;
    }
  }

  function waitForRenderer(timeoutMs) {
    return new Promise((resolve, reject) => {
      const started = Date.now();
      (function poll() {
        if (window.marked && window.DOMPurify) {
          resolve();
          return;
        }
        if (Date.now() - started > timeoutMs) {
          reject(new Error("The Markdown reader could not start. Check your internet connection and reload this page."));
          return;
        }
        setTimeout(poll, 30);
      })();
    });
  }

  function renderGuide(markdown) {
    if (typeof markdown !== "string" || markdown.length === 0) {
      throw new Error("Study guide markdown was empty.");
    }

    const rendered = window.marked.parse(markdown, { gfm: true, breaks: false });
    content.innerHTML = window.DOMPurify.sanitize(rendered, { USE_PROFILES: { html: true } });

    content.querySelectorAll('a[href^="http"]').forEach((link) => {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    });

    // Keep image URLs working from nested pages (e.g. /clf/).
    const imageBase = cfg.imageBase || "./";
    content.querySelectorAll("img[src]").forEach((img) => {
      const src = img.getAttribute("src") || "";
      if (/^(https?:|data:|\/)/i.test(src)) {
        return;
      }
      img.setAttribute("src", imageBase + src.replace(/^\.\//, ""));
    });

    const headings = buildNavigation();
    buildSearchIndex();

    const savedSection = getSavedSection();
    if (savedSection && content.querySelector(`#${CSS.escape(savedSection)}`)) {
      resumeButton.hidden = false;
      resumeButton.addEventListener("click", () => {
        document.getElementById(savedSection).scrollIntoView({ behavior: "smooth", block: "start" });
      }, { once: true });
    }

    let scrollScheduled = false;
    window.addEventListener("scroll", () => {
      updateProgress();
      if (!scrollScheduled) {
        scrollScheduled = true;
        window.requestAnimationFrame(() => {
          updateActiveNavigation(headings);
          scrollScheduled = false;
        });
      }
    }, { passive: true });
    updateProgress();
    updateActiveNavigation(headings);

    searchInput.addEventListener("input", runSearch);
    searchInput.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        searchInput.value = "";
        searchResults.hidden = true;
      }
    });
    document.addEventListener("keydown", (event) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        searchInput.focus();
      }
    });
  }

  async function loadGuide() {
    try {
      await waitForRenderer(8000);
      const markdownUrl = cfg.markdownUrl;
      if (!markdownUrl) {
        throw new Error("GUIDE_CONFIG.markdownUrl is missing.");
      }
      const response = await fetch(markdownUrl, { cache: "force-cache" });
      if (!response.ok) {
        throw new Error(`Could not load guide (${response.status}). Check that ${markdownUrl} is published.`);
      }
      const markdown = await response.text();
      renderGuide(markdown);
    } catch (error) {
      console.error("Unable to load the AWS learning guide.", error);
      showLoadError(error instanceof Error ? error.message : "Please check your connection and reload the page.");
    }
  }

  menuToggle.addEventListener("click", () => {
    const isOpen = sidebar.classList.toggle("is-open");
    backdrop.hidden = !isOpen;
    menuToggle.setAttribute("aria-expanded", String(isOpen));
  });
  backdrop.addEventListener("click", closeNavigation);

  function setLibraryOpen(open) {
    nav.hidden = !open;
    libraryToggle.setAttribute("aria-expanded", String(open));
    libraryToggle.classList.toggle("is-collapsed", !open);
    try {
      localStorage.setItem(libraryOpenKey, open ? "1" : "0");
    } catch (error) {
      console.warn("Could not save library open state.", error);
    }
  }

  libraryToggle.addEventListener("click", () => {
    const nextOpen = libraryToggle.getAttribute("aria-expanded") !== "true";
    setLibraryOpen(nextOpen);
  });

  try {
    if (localStorage.getItem(libraryOpenKey) === "0") {
      setLibraryOpen(false);
    }
  } catch (error) {
    // Ignore storage errors and keep library open.
  }

  loadGuide();
})();

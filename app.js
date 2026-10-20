(() => {
  const content = document.getElementById("markdown-content");
  const nav = document.getElementById("section-nav");
  const searchInput = document.getElementById("search-input");
  const searchResults = document.getElementById("search-results");
  const menuToggle = document.getElementById("menu-toggle");
  const sidebar = document.getElementById("sidebar");
  const backdrop = document.getElementById("sidebar-backdrop");
  const progress = document.getElementById("reading-progress");
  const sectionCount = document.getElementById("section-count");
  const resumeButton = document.getElementById("resume-button");
  const readingKey = "aws-ai-learning-last-section";

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

  function buildNavigation() {
    const headings = Array.from(content.querySelectorAll("h1, h2"));
    const usedIds = new Map();
    const fragment = document.createDocumentFragment();
    let sectionTotal = 0;

    headings.forEach((heading, index) => {
      const label = heading.textContent.trim();
      const baseId = slugify(label) || `section-${index + 1}`;
      const seen = usedIds.get(baseId) || 0;
      usedIds.set(baseId, seen + 1);
      heading.id = seen ? `${baseId}-${seen + 1}` : baseId;

      if (heading.tagName === "H1") {
        sectionTotal += 1;
      }

      const link = document.createElement("a");
      link.className = `nav-link${heading.tagName === "H2" ? " level-two" : ""}`;
      link.href = `#${heading.id}`;
      link.textContent = label;
      link.title = label;
      link.addEventListener("click", closeNavigation);
      fragment.append(link);
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

  function loadGuide() {
    try {
      if (!window.marked || !window.DOMPurify) {
        throw new Error("The Markdown reader could not start. Check your internet connection and reload this page.");
      }

      const markdown = window.GUIDE_MARKDOWN;
      if (typeof markdown !== "string" || markdown.length === 0) {
        throw new Error("Study guide content.js did not load. Confirm the file is published with the site.");
      }

      const rendered = window.marked.parse(markdown, { gfm: true, breaks: false });
      content.innerHTML = window.DOMPurify.sanitize(rendered, { USE_PROFILES: { html: true } });

      content.querySelectorAll('a[href^="http"]').forEach((link) => {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
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
    } catch (error) {
      console.error("Unable to load the AWS AI learning guide.", error);
      showLoadError(error instanceof Error ? error.message : "Please check your connection and reload the page.");
    }
  }

  menuToggle.addEventListener("click", () => {
    const isOpen = sidebar.classList.toggle("is-open");
    backdrop.hidden = !isOpen;
    menuToggle.setAttribute("aria-expanded", String(isOpen));
  });
  backdrop.addEventListener("click", closeNavigation);

  loadGuide();
})();

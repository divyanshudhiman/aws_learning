#!/usr/bin/env python3
"""Build study guide markdown from jwalsh/aif-c01 org sources (MIT)."""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path


def bash_path(unix_path: str) -> Path:
    out = subprocess.check_output(
        ["bash", "-lc", f"cygpath -w {unix_path}"],
        text=True,
    ).strip()
    return Path(out)


def convert_inline(s: str) -> str:
    def link_sub(match: re.Match[str]) -> str:
        inner = match.group(1)
        if "][" in inner:
            url, desc = inner.split("][", 1)
            if url.startswith("file:"):
                return desc
            return f"[{desc}]({url})"
        if inner.startswith("file:"):
            return ""
        return f"[{inner}]({inner})"

    s = re.sub(r"\[\[([^\]]+)\]\]", link_sub, s)
    s = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"**\1**", s)
    s = re.sub(r"(?<!\w)/([^/\n]+)/(?!\w)", r"*\1*", s)
    s = re.sub(r"=([^=\n]+)=", r"`\1`", s)
    s = re.sub(r"~([^~\n]+)~", r"`\1`", s)
    return s


def org_to_md(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    in_src = False
    src_lang = ""
    in_example = False
    skip_drawer = False

    pending_answer: list[str] = []

    for line in lines:
        stripped = line.strip()
        if re.match(r"^:(PROPERTIES|LOGBOOK):$", stripped):
            skip_drawer = True
            pending_answer = []
            continue
        if skip_drawer:
            if stripped == ":END:":
                skip_drawer = False
                if pending_answer:
                    out.extend(pending_answer)
                    out.append("")
                pending_answer = []
                continue
            answer = re.match(r"^:ANSWER:\s*(.*)$", stripped)
            if answer:
                pending_answer.append(f"**Answer:** {convert_inline(answer.group(1))}")
                continue
            explanation = re.match(r"^:EXPLANATION:\s*(.*)$", stripped)
            if explanation:
                pending_answer.append(f"**Explanation:** {convert_inline(explanation.group(1))}")
                continue
            continue

        match = re.match(r"#\+begin_src\s+(\S+)?", line, re.I)
        if match:
            in_src = True
            src_lang = match.group(1) or ""
            if src_lang.lower().startswith("mermaid"):
                out.append("_Diagram omitted in web notes._")
                out.append("")
                continue
            out.append(f"```{src_lang}")
            continue

        if re.match(r"#\+end_src", line, re.I):
            if in_src:
                if src_lang.lower().startswith("mermaid"):
                    in_src = False
                    src_lang = ""
                    continue
                in_src = False
                out.append("```")
            continue

        if in_src:
            if src_lang.lower().startswith("mermaid"):
                continue
            out.append(line)
            continue

        if re.match(r"#\+begin_example", line, re.I):
            in_example = True
            out.append("```")
            continue
        if re.match(r"#\+end_example", line, re.I):
            in_example = False
            out.append("```")
            continue
        if in_example:
            out.append(line)
            continue

        if re.match(r"#\+begin_quote", line, re.I) or re.match(r"#\+end_quote", line, re.I):
            continue

        match = re.match(r"#\+TITLE:\s*(.*)", line, re.I)
        if match:
            out.append(f"# {match.group(1).strip()}")
            out.append("")
            continue
        if line.startswith("#+"):
            continue
        # Org comments and Emacs local-variables footers (# Local Variables: … # End:)
        if re.match(r"^#\s", line):
            continue

        match = re.match(r"^(\*+)\s+(.*)$", line)
        if match:
            # TITLE becomes h1; org * headlines start at h2 for cleaner nesting.
            level = min(len(match.group(1)) + 1, 6)
            title = match.group(2).strip()
            title = re.sub(r"^(TODO|DONE|NEXT|WAITING)\s+", "", title)
            title = re.sub(r"\s+:[\w@:]+:\s*$", "", title)
            out.append("#" * level + " " + title)
            out.append("")
            continue

        if line.strip() == "-----":
            out.append("---")
            continue

        match = re.match(r"^(\s*)[-+]\s+(.*)$", line)
        if match:
            indent = match.group(1).replace("\t", "  ")
            out.append(f"{indent}- {convert_inline(match.group(2))}")
            continue

        match = re.match(r"^(\s*)(\d+)[.)]\s+(.*)$", line)
        if match:
            indent = match.group(1).replace("\t", "  ")
            out.append(f"{indent}{match.group(2)}. {convert_inline(match.group(3))}")
            continue

        if not line.strip():
            out.append("")
            continue

        out.append(convert_inline(line))

    text = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def main() -> None:
    src = bash_path("/tmp/aif-c01-src")
    dest_dir = Path(__file__).resolve().parents[1]
    print(f"source={src}")
    print(f"dest={dest_dir}")

    parts: list[str] = [
        """# AWS Certified AI Practitioner (AIF-C01) Study Guide

Personal study notes for the AIF-C01 exam.

**Source material:** Adapted from [jwalsh/aif-c01](https://github.com/jwalsh/aif-c01) by Jason Walsh, licensed under the [MIT License](https://github.com/jwalsh/aif-c01/blob/main/LICENSE). Copyright (c) Jason Walsh.

---
"""
    ]

    ordered = [
        "doc/aif-c01-notes.org",
        "doc/aws-ai-practitioner-course-outline.org",
        # ai-strategy-and-leadership.org upstream is malformed org; skipped.
        "aws-services-overview.org",
        "practice-tests/aif-c01-practice-01.org",
        "practice-tests/aif-c01-practice-02.org",
        "practice-tests/aif-c01-practice-03.org",
        "practice-tests/aif-c01-practice-04.org",
        "practice-tests/aif-c01-practice-05.org",
    ]

    for rel in ordered:
        raw = (src / rel).read_text(encoding="utf-8", errors="replace")
        parts.append(f"\n<!-- source: {rel} -->\n\n")
        parts.append(org_to_md(raw))
        parts.append("\n---\n")

    readme = (src / "README.org").read_text(encoding="utf-8", errors="replace")
    cut = re.search(r"^\* Project Workflow", readme, re.M)
    sections: list[str] = []
    sections.append(readme[: cut.start()] if cut else readme[:8000])

    for match in re.finditer(r"^\* (.+)$", readme, re.M):
        title = match.group(1).strip()
        if title in {"Project Workflow", "Introduction"}:
            continue
        keys = (
            "exam",
            "domain",
            "ai",
            "ml",
            "bedrock",
            "responsible",
            "service",
            "practice",
            "concept",
            "preparation",
            "study",
            "resource",
            "learning",
        )
        if not any(key in title.lower() for key in keys):
            continue
        start = match.start()
        nxt = re.search(r"^\* ", readme[match.end() :], re.M)
        end = match.end() + nxt.start() if nxt else len(readme)
        chunk = readme[start:end]
        if chunk.count("#+begin_src") > 8:
            continue
        sections.append(chunk)

    parts.append("\n# Additional materials from upstream README\n\n")
    parts.append(org_to_md("\n\n".join(sections)))

    out = re.sub(r"\n{3,}", "\n\n", "".join(parts))
    guide = dest_dir / "Comprehensive Scenario-Based Practice Question Bank.md"
    guide.write_text(out, encoding="utf-8")

    notices = dest_dir / "THIRD_PARTY_NOTICES.md"
    license_text = (src / "LICENSE").read_text(encoding="utf-8", errors="replace")
    notices.write_text(
        "# Third-party notices\n\n"
        "## jwalsh/aif-c01\n\n"
        "Study guide content adapted from:\n\n"
        "- Repository: https://github.com/jwalsh/aif-c01\n"
        "- Author: Jason Walsh\n"
        "- License: MIT\n\n"
        "```\n"
        f"{license_text.rstrip()}\n"
        "```\n",
        encoding="utf-8",
    )

    print(
        "guide",
        guide.name,
        "chars",
        len(out),
        "lines",
        out.count("\n"),
        "h1",
        len(re.findall(r"^# ", out, re.M)),
        "h2",
        len(re.findall(r"^## ", out, re.M)),
    )


if __name__ == "__main__":
    main()

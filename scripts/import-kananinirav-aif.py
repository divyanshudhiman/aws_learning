#!/usr/bin/env python3
"""Build study guide markdown from kananinirav/aws-certified-ai-practitioner-study-notes (MIT)."""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path


def bash_path(unix_path: str) -> Path:
    out = subprocess.check_output(
        ["bash", "-lc", f"cygpath -w {unix_path}"],
        text=True,
    ).strip()
    return Path(out)


def rewrite_images(md: str) -> str:
    # Normalize all relative image paths to ./images/<file>
    def repl(match: re.Match[str]) -> str:
        alt, url = match.group(1), match.group(2)
        if url.startswith(("http://", "https://", "data:")):
            return match.group(0)
        name = Path(url.replace("\\", "/")).name
        return f"![{alt}](./images/{name})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl, md)


def strip_html_comments(md: str) -> str:
    return re.sub(r"<!--.*?-->", "", md, flags=re.S)


def main() -> None:
    src = bash_path("/tmp/kanan-aif")
    dest = Path(__file__).resolve().parents[1]
    print(f"source={src}")
    print(f"dest={dest}")

    images_src = src / "images"
    images_dest = dest / "images"
    if images_src.is_dir():
        if images_dest.exists():
            shutil.rmtree(images_dest)
        shutil.copytree(images_src, images_dest)
        print(f"copied images -> {images_dest}")

    ordered = [
        "study-guide.md",
        "section/cloud-computing/cloud-computing.md",
        "section/gen-ai/genai-introduction.md",
        "section/gen-ai/amazon-bedrock.md",
        "section/gen-ai/prompt-engineering.md",
        "section/gen-ai/amazon-q.md",
        "section/ai-and-ml/ai-and-ml-introduction.md",
        "section/aws-managed-ai-services/introduction-of-aws-managed-ai-services.md",
        "section/aws-managed-ai-services/aws-comprehend.md",
        "section/aws-managed-ai-services/aws-translate.md",
        "section/aws-managed-ai-services/aws-transcribe.md",
        "section/aws-managed-ai-services/aws-polly.md",
        "section/aws-managed-ai-services/aws-rekognition.md",
        "section/aws-managed-ai-services/aws-lex.md",
        "section/aws-managed-ai-services/aws-personalize.md",
        "section/aws-managed-ai-services/aws-textract.md",
        "section/aws-managed-ai-services/aws-kendra.md",
        "section/aws-managed-ai-services/aws-mechanical-turk.md",
        "section/aws-managed-ai-services/aws-augmented-ai.md",
        "section/aws-managed-ai-services/ai-hardware.md",
        "section/aws-managed-ai-services/aws-ai-services-summary.md",
        "section/sagemaker/aws-sagemaker.md",
        "section/ai-challenges-and-responsibilities/responsible-ai.md",
        "section/ai-challenges-and-responsibilities/genai-challenges.md",
        "section/ai-challenges-and-responsibilities/compliance.md",
        "section/ai-challenges-and-responsibilities/governance.md",
        "section/ai-challenges-and-responsibilities/security-and-privacy.md",
        "section/ai-challenges-and-responsibilities/mlops.md",
        "section/aws-security-services/aws-security-services.md",
        "glossary.md",
        "practice-test/tests.md",
        "practice-test/practice-test-1.md",
        "practice-test/practice-test-2.md",
        "practice-test/practice-test-3.md",
        "practice-test/practice-test-4.md",
        "practice-test/practice-test-5.md",
        "practice-test/practice-test-6.md",
        "practice-test/practice-test-7.md",
    ]

    parts: list[str] = [
        """# AWS Certified AI Practitioner (AIF-C01) Study Guide

Personal study notes for the AIF-C01 exam.

**Primary source:** Adapted from [kananinirav/aws-certified-ai-practitioner-study-notes](https://github.com/kananinirav/aws-certified-ai-practitioner-study-notes) by kananinirav, licensed under the [MIT License](https://github.com/kananinirav/aws-certified-ai-practitioner-study-notes/blob/master/LICENSE). Copyright (c) 2026 kananinirav.

**Also credited:** Earlier material adapted from [jwalsh/aif-c01](https://github.com/jwalsh/aif-c01) (MIT). See `THIRD_PARTY_NOTICES.md`.

---
"""
    ]

    for rel in ordered:
        path = src / rel
        if not path.is_file():
            print(f"missing: {rel}")
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        raw = strip_html_comments(raw)
        raw = rewrite_images(raw).strip()
        parts.append(f"\n<!-- source: {rel} -->\n\n")
        parts.append(raw)
        parts.append("\n\n---\n")

    out = re.sub(r"\n{3,}", "\n\n", "".join(parts)).strip() + "\n"
    guide = dest / "Comprehensive Scenario-Based Practice Question Bank.md"
    guide.write_text(out, encoding="utf-8")

    license_text = (src / "LICENSE").read_text(encoding="utf-8", errors="replace")
    notices = dest / "THIRD_PARTY_NOTICES.md"
    existing = notices.read_text(encoding="utf-8") if notices.exists() else ""
    if "kananinirav" not in existing:
        block = (
            "\n## kananinirav/aws-certified-ai-practitioner-study-notes\n\n"
            "Study guide content adapted from:\n\n"
            "- Repository: https://github.com/kananinirav/aws-certified-ai-practitioner-study-notes\n"
            "- Author: kananinirav\n"
            "- License: MIT\n\n"
            "```\n"
            f"{license_text.rstrip()}\n"
            "```\n"
        )
        if existing.strip():
            notices.write_text(existing.rstrip() + "\n" + block, encoding="utf-8")
        else:
            notices.write_text("# Third-party notices\n" + block, encoding="utf-8")

    print(
        "guide",
        guide.name,
        "chars",
        len(out),
        "lines",
        out.count("\n"),
        "h1",
        len(re.findall(r"^# ", out, re.M)),
        "images",
        len(list(images_dest.glob("*"))) if images_dest.exists() else 0,
    )


if __name__ == "__main__":
    main()

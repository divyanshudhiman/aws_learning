#!/usr/bin/env python3
"""Restructure the AIF-C01 study guide and enrich thin definitions with examples."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "guides" / "aif-c01.md"

# Map original H1 titles (normalized) -> (part_key, display_as_h2)
PARTS = [
    ("part-exam", "Part 0 - Exam Overview"),
    ("part-cloud", "Part 1 - Cloud Foundations"),
    ("part-genai", "Part 2 - Generative AI and Amazon Bedrock"),
    ("part-aiml", "Part 3 - AI and Machine Learning Fundamentals"),
    ("part-managed", "Part 4 - AWS Managed AI Services"),
    ("part-sagemaker", "Part 5 - Amazon SageMaker"),
    ("part-responsible", "Part 6 - Responsible AI, Security and Governance"),
    ("part-security", "Part 7 - AWS Security Services for AI"),
    ("part-glossary", "Part 8 - Glossary"),
    ("part-practice", "Part 9 - Practice Tests"),
]

H1_TO_PART = {
    "aws certified ai practitioner (aif-c01) study guide": "part-exam",
    "cloud computing": "part-cloud",
    "genai introduction": "part-genai",
    "amazon bedrock": "part-genai",
    "prompt engineering": "part-genai",
    "amazon q": "part-genai",
    "ai and machine learning overview": "part-aiml",
    "introduction of aws managed ai services": "part-managed",
    "amazon comprehend": "part-managed",
    "amazon translate": "part-managed",
    "amazon transcribe": "part-managed",
    "amazon polly": "part-managed",
    "amazon rekognition": "part-managed",
    "amazon lex": "part-managed",
    "amazon personalize": "part-managed",
    "amazon textract": "part-managed",
    "amazon kendra": "part-managed",
    "amazon mechanical turk": "part-managed",
    "amazon augmented ai (a2i)": "part-managed",
    "hardware for ai": "part-managed",
    "aws managed ai services - quick revision summary": "part-managed",
    "amazon sagemaker": "part-sagemaker",
    "responsible ai and security": "part-responsible",
    "genai capabilities and challenges": "part-responsible",
    "compliance for ai": "part-responsible",
    "governance for ai": "part-responsible",
    "security and privacy for ai systems": "part-responsible",
    "mlops (machine learning operations)": "part-responsible",
    "aws security services and more": "part-security",
    "aws ai practitioner test study notes - glossary": "part-glossary",
    "practice tests": "part-practice",
    "practice test 1": "part-practice",
    "practice test 2": "part-practice",
    "practice test 3": "part-practice",
    "practice test 4": "part-practice",
    "practice test 5": "part-practice",
    "practice test 6": "part-practice",
    "practice test 7": "part-practice",
}

# Extra examples keyed by heading substring (lowercase). Injected once per matching section.
EXAMPLES: dict[str, str] = {
    "what is generative ai": """
#### Worked examples

| Scenario | Traditional AI | Generative AI |
| --- | --- | --- |
| Support tickets | Classify as billing / tech / cancel | Draft a polite reply to the customer |
| Product photos | Detect if image contains a shoe | Create a lifestyle image of the shoe on a beach |
| Code review | Flag a security smell | Suggest a patched function |

**Exam tip:** If the task is *create* new content (text, image, code), think GenAI; if the task is *label / detect / predict* on existing data, think classic ML.
""",
    "how it differs from traditional ai": """
#### Quick examples

- **Traditional:** “Is this email spam?” → classification
- **Generative:** “Rewrite this email in a friendlier tone” → content creation
- **Hybrid (common on AWS):** Transcribe a call (ASR) → summarize with an LLM (GenAI)
""",
    "foundation model": """
#### Examples

- **General text FM:** Anthropic Claude or Amazon Titan Text on Amazon Bedrock
- **Image FM:** Stable Diffusion via Bedrock for marketing creatives
- **Embedding FM:** Titan Embeddings to power RAG search over PDFs

**Business example:** A retailer uses one FM for product descriptions, another embedding model for semantic search, without training either from scratch.
""",
    "large language models": """
#### Examples

- Prompt: “Summarize this 20-page contract in 5 bullets for a CFO” → LLM summarization
- Prompt: “Convert this Python function to TypeScript” → code generation
- Prompt: “Extract invoice number, date, and total from this text” → structured extraction

**Contrast:** An LLM is a *type* of foundation model specialized for language; not every FM is an LLM (e.g., image or speech models).
""",
    "what is a vector database": """
#### Examples

1. Embed company wiki pages → store vectors in OpenSearch Serverless / pgvector
2. User asks “How do we reset MFA?” → embed question → nearest-neighbor search → pass top chunks to an LLM (RAG)
3. Product catalog: similar-item search by meaning (“waterproof hiking boots”) not exact keywords

**Why it matters for AIF-C01:** Vector DBs are the memory layer that makes RAG accurate on private data.
""",
    "what is rag (retrieval-augmented generation)": """
#### End-to-end example

1. HR policies live in S3
2. Bedrock Knowledge Bases indexes them into a vector store
3. Employee asks: “How many PTO days after 2 years?”
4. System retrieves the relevant policy paragraph
5. LLM answers **using that paragraph**, reducing hallucinations

**When RAG beats fine-tuning:** Policies change weekly; re-index docs instead of re-training a model.
""",
    "fine-tuning a model": """
#### Examples

- **Domain language:** Fine-tune on legal contracts so outputs use firm-specific phrasing
- **Task style:** Fine-tune for consistent JSON ticket fields for a helpdesk bot
- **Not fine-tuning:** Prompt templates + RAG for FAQ answers (cheaper, faster to update)

**Exam tip:** Prefer fine-tuning when you need a *stable new behavior*; prefer RAG when you need *current private facts*.
""",
    "what is prompt engineering": """
#### Before / after examples

- Weak: “Write about Bedrock.”
- Strong: “You are an AWS solutions architect. In 5 bullets, explain when to choose Amazon Bedrock over SageMaker JumpStart for a GenAI chatbot. Audience: non-technical PM.”

- Weak: “Extract entities.”
- Strong: “Extract `person`, `org`, `date` as JSON only. If unknown, use null. Text: …”
""",
    "negative prompting": """
#### Examples

- Image: “city skyline at dusk” + negative: “blurry, watermark, text, low quality”
- Text: “Write a product FAQ” + negative: “do not mention competitors or pricing discounts”
""",
    "prompt engineering techniques": """
#### Technique → example

| Technique | Example prompt fragment |
| --- | --- |
| Zero-shot | “Translate to French: …” |
| Few-shot | Show 2 sample Q&A pairs, then ask the real question |
| Chain-of-thought | “Think step by step, then give the final answer.” |
| Role prompting | “You are a security auditor reviewing IAM policies…” |
| Template | System prompt + user variables filled at runtime |
""",
    "what is amazon bedrock": """
#### Examples

- Invoke Claude on Bedrock via API for a customer chatbot (no GPU servers to manage)
- Use Bedrock Guardrails to block PII and hate speech in outputs
- Use Bedrock Knowledge Bases for RAG over internal PDFs
- Use Bedrock Agents to call Lambda tools (check order status)
""",
    "what is ai": """
#### Everyday examples

- Spam filter that decides spam vs not spam
- Maps that predict traffic and suggest a route
- Voice assistants that turn speech into actions
- Fraud systems that score a credit-card charge as risky
""",
    "what is machine learning (ml)": """
#### Learning-type examples

| Type | Example |
| --- | --- |
| Supervised | Predict house price from size/location (labels = past sale prices) |
| Unsupervised | Cluster customers into segments with no pre-set labels |
| Reinforcement | Game agent learns moves by reward/penalty |
| Self-supervised | LLM predicts masked words in text (labels from the text itself) |
""",
    "what is deep learning (dl)": """
#### Examples

- Image classification with CNNs (cat vs dog photos)
- Speech recognition with deep ASR models (Amazon Transcribe)
- Transformers for language (LLMs)

**Note:** Deep Learning is a subset of ML that uses multi-layer neural networks.
""",
    "what is deep leaning(dl)": """
#### Examples

- Image classification with CNNs (cat vs dog photos)
- Speech recognition with deep ASR models (Amazon Transcribe)
- Transformers for language (LLMs)

**Note:** Deep Learning is a subset of ML that uses multi-layer neural networks.
""",
    "supervised learning": """
#### Examples

- Email labeled spam/ham → train a classifier
- Historical churn labels → predict which customers will leave
- Labeled X-rays → detect pneumonia

**Requirement:** You need labeled examples. On AWS, SageMaker Ground Truth / A2I help create labels.
""",
    "unsupervised learning": """
#### Examples

- Group news articles by topic without tags
- Detect unusual login patterns (anomaly detection)
- Compress features with PCA for visualization
""",
    "reinforcement learning (rl)": """
#### Examples

- Robot arm learns to pick objects via reward for successful grasps
- Ad bidding agent learns bids that maximize conversions
- RLHF: humans rank LLM answers; model learns preferred style
""",
    "what is rlhf": """
#### Example flow

1. LLM drafts three answers to “Explain IAM roles”
2. Human ranks them best → worst
3. Reward model trains on rankings
4. Policy is optimized so future answers match preferred style (helpful, safe, clear)
""",
    "model fit": """
#### Examples

- **Underfit:** Linear model on curved data → high train & test error
- **Good fit:** Errors low on train and test
- **Overfit:** Near-zero train error, poor test error → memorize noise

**Fix overfitting:** more data, regularization, dropout, simpler model, early stopping.
""",
    "bias and variance": """
#### Intuition examples

- **High bias:** Always predicts “average house price” → systematically wrong
- **High variance:** Tiny change in training set wildly changes predictions
""",
    "confusion matrix": """
#### Example (fraud detection)

|  | Predicted Fraud | Predicted OK |
| --- | --- | --- |
| Actual Fraud | TP | FN (missed fraud) |
| Actual OK | FP (false alarm) | TN |

**Business choice:** Banks often accept more FP to reduce FN (missed fraud).
""",
    "amazon comprehend": """
#### Scenario examples

- Support inbox → sentiment + key phrases → route angry VIP tickets first
- News feed → NER for companies/people → alert on competitor mentions
- Custom classification → “returns”, “billing”, “tech” email categories
""",
    "amazon translate": """
#### Examples

- Localize product descriptions EN → ES/DE/JA for an ecommerce site
- Custom terminology so “Amazon Bedrock” is never mistranslated
- Detect language of inbound chat, then translate to agent’s language
""",
    "amazon transcribe": """
#### Examples

- Call-center recordings → searchable transcripts
- Live captioning for meetings (streaming)
- Medical dictation with Transcribe Medical
""",
    "amazon polly": """
#### Examples

- Accessibility: convert blog posts to audio
- IVR prompts with consistent brand voice
- SSML to slow speech and add pauses for tutorials
""",
    "amazon rekognition": """
#### Examples

- Moderate user-uploaded images (nudity, violence)
- Detect PPE (helmets) on factory camera frames
- Celebrity recognition for media archives
""",
    "amazon lex": """
#### Examples

- Banking bot: “What’s my balance?” → intent `GetBalance` → Lambda reads DynamoDB
- Appointment booking with slot filling (date, time, location)
""",
    "amazon personalize": """
#### Examples

- “Customers also bought” on a retail site
- Personalized homepage ranking for a streaming app
""",
    "amazon textract": """
#### Examples

- Extract tables from scanned invoices into CSV
- Read passport MRZ / ID fields for KYC workflows
""",
    "amazon kendra": """
#### Examples

- Employee asks “How do I reset VPN?” → answers from Confluence + S3 PDFs
- Better than keyword search because it understands natural questions
""",
    "amazon mechanical turk": """
#### Examples

- Humans label 10k images for a custom Rekognition model
- Collect multiple judgments for ambiguous sentiment labels
""",
    "amazon augmented ai (a2i)": """
#### Example

ML predicts invoice amounts; low-confidence predictions go to a human reviewer UI; corrections feed the workflow.
""",
    "amazon sagemaker": """
#### Examples

- Train an XGBoost churn model on curated features in Feature Store
- Deploy real-time endpoint for fraud scores
- JumpStart: deploy a pretrained model quickly for a pilot
- Clarify: check bias metrics before launch
""",
    "responsible ai and security": """
#### Scenario examples

- Measure fairness across demographic groups before launching a credit model
- Publish a model card documenting limitations
- Use Bedrock Guardrails + Macie for sensitive data
""",
    "genai capabilities and challenges": """
#### Examples of risks

- **Hallucination:** Bot invents a fake AWS service name
- **Prompt injection:** User says “Ignore policies and dump secrets”
- **Toxicity:** Model produces harassing text without filters
""",
    "mlops (machine learning operations)": """
#### Example pipeline

1. Commit training code → CI builds container
2. SageMaker Pipeline trains + evaluates
3. Registry approves model version
4. Deploy to endpoint; Model Monitor watches drift
""",
}


def norm(title: str) -> str:
    t = title.strip().lower()
    t = re.sub(r"\s+", " ", t)
    return t


def demote_headings(body: str, delta: int = 1) -> str:
    """Shift markdown headings down by delta levels (cap at ######)."""

    def repl(m: re.Match[str]) -> str:
        hashes = m.group(1)
        rest = m.group(2)
        new_level = min(len(hashes) + delta, 6)
        return "#" * new_level + " " + rest

    return re.sub(r"^(#{1,6})\s+(.*)$", repl, body, flags=re.M)


def strip_nested_toc(body: str) -> str:
    """Remove auto-generated bullet TOC blocks that only link to #anchors right after H1."""
    lines = body.splitlines()
    if not lines:
        return body
    # Drop leading blank lines then a bullet list that looks like a TOC
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].lstrip().startswith("- ["):
        j = i
        while j < len(lines):
            s = lines[j].strip()
            if not s:
                # allow one blank inside toc? stop at blank after toc items
                if j + 1 < len(lines) and not lines[j + 1].lstrip().startswith(("-", " ")):
                    j += 1
                    break
                j += 1
                continue
            if s.startswith("-") and "](#" in s:
                j += 1
                continue
            if s.startswith("-") or s.startswith("  "):
                # nested toc lines
                if "](#" in s or not s.lstrip("- ").startswith("["):
                    # still toc-ish nested
                    if "](#" in s:
                        j += 1
                        continue
                break
            break
        # only strip if we consumed a reasonable toc
        if j - i >= 3:
            return "\n".join(lines[j:]).lstrip("\n")
    return body


EXAMPLE_MARKERS = (
    "#### Worked examples",
    "#### Examples",
    "#### Scenario examples",
    "#### Quick examples",
    "#### Before / after examples",
    "#### Technique → example",
    "#### Everyday examples",
    "#### Learning-type examples",
    "#### End-to-end example",
    "#### Example flow",
    "#### Intuition examples",
    "#### Example pipeline",
    "#### Example",
    "#### Example (",
)


def lookup_example(title: str) -> str | None:
    key = norm(title)
    # Prefer exact / near-exact matches only to avoid spraying one block across many headings.
    if key in EXAMPLES:
        return EXAMPLES[key].strip("\n")
    for k, v in EXAMPLES.items():
        if key == k:
            return v.strip("\n")
        # Allow minor punctuation differences
        if re.sub(r"[^a-z0-9]+", "", key) == re.sub(r"[^a-z0-9]+", "", k):
            return v.strip("\n")
    for k, v in EXAMPLES.items():
        # Title contains full example key as a phrase (e.g. heading longer than key)
        if len(k) >= 12 and k in key:
            return v.strip("\n")
        # Example key contains full title when title is specific enough
        if len(key) >= 12 and key in k:
            return v.strip("\n")
    return None


def inject_examples_into_body(body: str, section_title: str = "") -> str:
    """Inject example blocks after matching ## / ### headings inside a section body."""
    # Also try section-level match once at end of intro (before first ##)
    chunks = re.split(r"(?m)^(#{2,3}\s+.+)$", body)
    out: list[str] = []
    # preamble
    preamble = chunks[0]
    section_ex = lookup_example(section_title) if section_title else None
    if section_ex and not any(m in preamble for m in EXAMPLE_MARKERS):
        # Only attach to thin preambles (< 25 non-empty lines)
        nonempty = [ln for ln in preamble.splitlines() if ln.strip()]
        if len(nonempty) <= 25:
            preamble = preamble.rstrip() + "\n\n" + section_ex + "\n"
    out.append(preamble)

    i = 1
    while i < len(chunks):
        heading = chunks[i]
        content = chunks[i + 1] if i + 1 < len(chunks) else ""
        title = re.sub(r"^#{2,3}\s+", "", heading).strip()
        block = lookup_example(title)
        if block and not any(m in content for m in EXAMPLE_MARKERS):
            content = content.rstrip() + "\n\n" + block + "\n"
        out.append(heading + "\n")
        out.append(content)
        i += 2
    return "".join(out)


def inject_examples(title: str, body: str) -> str:
    return inject_examples_into_body(body, section_title=title)


def split_h1_sections(text: str) -> list[tuple[str | None, str]]:
    """Return list of (h1_title_or_None, section_text_including_heading)."""
    parts: list[tuple[str | None, str]] = []
    # Split keeping delimiters
    chunks = re.split(r"(?m)^(#[^#].*)$", text)
    # chunks[0] is preamble before first H1
    if chunks[0].strip():
        parts.append((None, chunks[0]))
    i = 1
    while i < len(chunks):
        heading = chunks[i].strip()
        body = chunks[i + 1] if i + 1 < len(chunks) else ""
        title = re.sub(r"^#\s+", "", heading).strip()
        parts.append((title, heading + "\n" + body))
        i += 2
    return parts


def fix_typos(text: str) -> str:
    replacements = {
        "Deep Leaning(DL)": "Deep Learning (DL)",
        "Deep Leaning": "Deep Learning",
        "what is deep leaning": "what is deep learning",
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    return text


def build_master_toc(part_order: list[str], part_titles: dict[str, str], sections_by_part: dict[str, list[str]]) -> str:
    lines = ["## How to use this guide", "", "Study in order of exam weight, then drill practice tests.", ""]
    lines.append("| Part | Focus |")
    lines.append("| --- | --- |")
    for key in part_order:
        lines.append(f"| {part_titles[key]} | {len(sections_by_part.get(key, []))} sections |")
    lines.append("")
    lines.append("**Suggested path:** Exam overview → GenAI/Bedrock → AI/ML fundamentals → Managed services → SageMaker → Responsible AI → Practice tests.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    raw = GUIDE.read_text(encoding="utf-8")
    raw = fix_typos(raw)

    # Keep attribution header (everything before first real content H1 after attribution)
    sections = split_h1_sections(raw)

    part_order = [p[0] for p in PARTS]
    part_titles = {p[0]: p[1] for p in PARTS}
    sections_by_part: dict[str, list[tuple[str, str]]] = {k: [] for k in part_order}
    orphan: list[tuple[str, str]] = []

    preamble_bits: list[str] = []
    first_exam_done = False

    for title, block in sections:
        if title is None:
            preamble_bits.append(block)
            continue
        ntitle = norm(title)
        part = H1_TO_PART.get(ntitle)
        if part is None:
            # try fuzzy contains
            for k, v in H1_TO_PART.items():
                if k in ntitle or ntitle in k:
                    part = v
                    break
        if part is None:
            orphan.append((title, block))
            continue

        # Extract body without the H1 line
        lines = block.splitlines()
        body = "\n".join(lines[1:])
        body = strip_nested_toc(body)

        # Skip the short attribution-only shell H1 from prior imports
        if part == "part-exam":
            body = re.sub(
                r"(?is)^\s*Personal study notes.*?THIRD_PARTY_NOTICES\.md`\.\s*(---\s*)?",
                "",
                body,
                count=1,
            )
            body = re.sub(
                r"(?is)^\s*Structured personal study notes.*?THIRD_PARTY_NOTICES\.md`\.\s*(---\s*)?",
                "",
                body,
                count=1,
            )
            if len(body.strip()) < 500:
                continue
            if first_exam_done and "study guide" in ntitle:
                continue
            first_exam_done = True

        body = inject_examples(title, body)
        # Demote internal headings by 1 because this H1 becomes H2 under a Part H1
        # (example #### blocks become ##### which is fine)
        body = demote_headings(body, 1)
        new_block = f"## {title}\n{body}".rstrip() + "\n"
        sections_by_part[part].append((title, new_block))

    # Attribution preamble: keep only the short header (first ~10 non-empty lines of original)
    header = """# AWS Certified AI Practitioner (AIF-C01) Study Guide

Structured personal study notes for the AIF-C01 exam — reorganized by topic with extra worked examples on key definitions.

**Primary source:** Adapted from [kananinirav/aws-certified-ai-practitioner-study-notes](https://github.com/kananinirav/aws-certified-ai-practitioner-study-notes) (MIT). Copyright (c) 2026 kananinirav.

**Also credited:** [jwalsh/aif-c01](https://github.com/jwalsh/aif-c01) (MIT). See `THIRD_PARTY_NOTICES.md`.

**Edition note:** Structure grouped into Parts 0–9; thin definitions expanded with scenario examples for exam recall.

---
"""

    out: list[str] = [header]
    out.append(build_master_toc(part_order, part_titles, {k: [t for t, _ in v] for k, v in sections_by_part.items()}))
    out.append("---\n")

    for key in part_order:
        items = sections_by_part.get(key) or []
        if not items:
            continue
        out.append(f"# {part_titles[key]}\n")
        for _title, block in items:
            out.append(block)
            out.append("\n---\n")

    if orphan:
        out.append("# Additional notes\n")
        for title, block in orphan:
            lines = block.splitlines()
            body = "\n".join(lines[1:])
            body = strip_nested_toc(body)
            body = demote_headings(body, 1)
            out.append(f"## {title}\n{body}\n\n---\n")

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Fix double-demotion of already #### examples inside demoted content - ensure examples stay readable
    GUIDE.write_text(text, encoding="utf-8")
    print(
        "wrote",
        GUIDE.name,
        "chars",
        len(text),
        "lines",
        text.count("\n"),
        "h1",
        len(re.findall(r"^# ", text, re.M)),
        "h2",
        len(re.findall(r"^## ", text, re.M)),
        "example_blocks",
        text.count("#### "),
    )


if __name__ == "__main__":
    main()

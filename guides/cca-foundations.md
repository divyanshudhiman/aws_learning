# Claude Certified Architect – Foundations Study Guide

In-depth personal study notes for the **Claude Certified Architect – Foundations** certification — same study pattern as the AWS guides on this site: starter definitions, domain deep-dives, glossary, and scenario practice with answers.

**Important:** This is an unofficial study aid. It is **not** published by Anthropic. Exam eligibility is typically limited to organizations in the Claude Partner Network — confirm current rules on Anthropic’s certification pages before registering.

**Companion guides:** [AIF-C01](../) · [CLF-C02](../clf/)

**Official prep pointers:** Anthropic exam guide (PDF via Skilljar/partner portal) · hands-on practice with Claude API, Agent SDK, Claude Code, and MCP.

---

## How to use this guide

| Part | Focus |
| --- | --- |
| Part 0 - Essential Definitions | Starter glossary |
| Part 1 - Exam Overview | Format, scenarios, weightings |
| Part 2 - Agentic Architecture & Orchestration | Domain 1 (27%) |
| Part 3 - Tool Design & MCP Integration | Domain 2 (18%) |
| Part 4 - Claude Code Configuration & Workflows | Domain 3 (20%) |
| Part 5 - Prompt Engineering & Structured Output | Domain 4 (20%) |
| Part 6 - Context Management & Reliability | Domain 5 (15%) |
| Part 7 - Production Scenarios Map | Six exam scenario frames |
| Part 8 - Glossary | Term cheat sheet |
| Part 9 - Practice Tests | Scenarios with answers |

**Suggested path:** Definitions → Exam overview → Domains 1→5 by weight → Scenario map → Practice tests. Pair every Part with hands-on coding.

---

# Part 0 - Essential Definitions (Start Here)

## Platform building blocks

| Term | Plain meaning | Exam angle |
| --- | --- | --- |
| **Claude API** | HTTP/SDK access to Claude models for apps you build | Messages, tools, system prompts |
| **Claude Agent SDK** | Higher-level SDK for agent loops, tools, subagents, hooks | Production agents and orchestration |
| **Claude Code** | Agent-first coding CLI/IDE workflow product | CLAUDE.md, slash commands, plan mode, CI `-p` |
| **MCP (Model Context Protocol)** | Open protocol for tools/resources servers Claude can call | Custom backends + shared servers |
| **Tool** | Function the model can invoke with structured args | Selection depends on **descriptions** |
| **Resource (MCP)** | Catalog/content the client can read without a tool call | Reduce exploratory calls |
| **Agentic loop** | Request → maybe tool_use → execute → feed results → repeat until end | Driven by `stop_reason` |
| **stop_reason** | Why the model stopped (`tool_use`, `end_turn`, …) | Loop while `tool_use`; stop on `end_turn` |
| **Coordinator / subagent** | Hub agent delegates to specialized agents | Isolated contexts; explicit handoffs |
| **Task tool** | Mechanism to spawn subagents | Coordinator needs Task in allowed tools |
| **Hook** | Deterministic intercept of tool calls/results | Prefer over prompts for hard rules |
| **CLAUDE.md** | Persistent instructions/memory for Claude Code | Hierarchy: user / project / directory |
| **Plan mode** | Explore and design before large edits | Complex multi-file / architecture work |
| **tool_choice** | `auto` / `any` / force named tool | Force first step or require a tool call |
| **Structured output** | Schema-constrained JSON (often via tool_use) | Syntax ≠ semantic correctness |
| **Human-in-the-loop** | Escalate/confirm before risky actions | Refunds, ambiguous policy cases |

## Reliability vocabulary

| Term | Meaning |
| --- | --- |
| **Hallucination** | Fluent but false content |
| **Grounding** | Tie answers to retrieved/tool facts |
| **False positive** | Flagging something that is fine (kills trust in reviews) |
| **Context window** | Max tokens of prompt + history the model can see |
| **Context pollution** | Noisy/irrelevant tokens that dilute attention |
| **Session resume** | Continue a named prior session |
| **Fork session** | Branch from a baseline to explore alternatives |
| **Stale tool results** | Old file/API snapshots that mislead resumed work |

## Don’t-mix pairs

| A | B | Difference |
| --- | --- | --- |
| Prompt enforcement | Hook enforcement | Probabilistic vs deterministic |
| Plan mode | Direct execution | Design first vs small clear changes |
| Grep | Glob | Search **contents** vs match **paths** |
| Edit | Write | Targeted patch vs full file rewrite |
| Project MCP (`.mcp.json`) | User MCP (`~/.claude.json`) | Shared team vs personal |
| CLAUDE.md always-on | Slash skill on-demand | Universal standards vs task workflows |
| tool_choice auto | tool_choice any | May chat vs must call a tool |
| Schema-valid JSON | Semantically correct JSON | Parses ≠ business-true |

---

# Part 1 - Exam Overview

## What the cert validates

You can make **informed tradeoffs** when building production solutions with Claude across Claude Code, the Claude Agent SDK, the Claude API, and Model Context Protocol (MCP).

Not just definitions — **judgment** under realistic constraints.

## Candidate profile (typical)

- Solution architect building production Claude apps
- About **6+ months** hands-on with API, Agent SDK, Claude Code, MCP
- Comfortable with multi-agent orchestration, tool design, structured output, CI integration, escalation/reliability

## Format (publicly reported)

| Item | Typical value |
| --- | --- |
| Questions | ~60 multiple choice (1 correct + 3 distractors) |
| Time | ~120 minutes |
| Style | Scenario-framed (4 of 6 production scenarios per sitting) |
| Score | Scaled 100–1000; pass about **720** |
| Delivery | Proctored (confirm current process) |

Unanswered = incorrect; no guessing penalty beyond that.

## Domains and weightings

| Domain | Weight |
| --- | --- |
| 1. Agentic Architecture & Orchestration | **27%** |
| 2. Tool Design & MCP Integration | **18%** |
| 3. Claude Code Configuration & Workflows | **20%** |
| 4. Prompt Engineering & Structured Output | **20%** |
| 5. Context Management & Reliability | **15%** |

**Study bias:** Domain 1 is heaviest; Domains 3 and 4 together are 40%.

---

# Part 2 - Agentic Architecture & Orchestration (27%)

## 2.1 The agentic loop

**Correct control flow**

1. Send messages (+ tools) to Claude
2. Inspect `stop_reason`
3. If `tool_use` → execute tools → **append tool results** to history → loop
4. If `end_turn` → stop

**Anti-patterns**

- Parsing assistant prose (“DONE”) to decide when to stop
- Relying on arbitrary max-iteration caps as the *primary* stop signal
- Treating “assistant produced text” as completion while tools still pending

**Model-driven vs hard-coded trees:** the model chooses the next tool from context; you don’t pre-script every branch unless compliance requires programmatic gates.

##### Example

Support agent calls `lookup_order` → sees missing identity → must call `get_customer` before `process_refund`. Loop continues until `end_turn` after resolution or escalation.

## 2.2 Coordinator + subagents

**Hub-and-spoke**

- Coordinator: decompose, delegate, aggregate, error-handle, decide next steps
- Subagents: **isolated context** — they do **not** inherit parent history automatically
- Pass needed findings **explicitly** in the subagent prompt (structured: content + provenance metadata)

**Task tool**

- Spawning uses Task (or equivalent Agent SDK spawn)
- Coordinator `allowedTools` must include Task
- Parallelism: emit **multiple Task calls in one coordinator turn** when independent

**Decomposition risks**

- Overly narrow splits → incomplete coverage on broad research
- Always running the full pipeline when a subset of specialists would suffice

**Refinement loop:** evaluate synthesis for gaps → re-delegate targeted searches → re-synthesize.

## 2.3 Workflow enforcement & handoffs

| Need | Prefer |
| --- | --- |
| Soft guidance | Prompt instructions |
| Hard business rule (ID before refund) | **Programmatic gate / hook** |
| Mid-process human escalation | **Structured handoff** (IDs, root cause, recommended action) |

Prompt-only ordering has **non-zero failure rate** — don’t trust it for money/security steps.

## 2.4 Hooks

- **Outgoing intercept:** block policy violations (refund over threshold → escalate)
- **PostToolUse:** normalize messy tool payloads (timestamps, status codes) before the model sees them
- Hooks = **deterministic**; prompts = **probabilistic**

## 2.5 Decomposition strategies

| Pattern | When |
| --- | --- |
| Fixed prompt chaining | Predictable multi-aspect reviews |
| Adaptive decomposition | Open-ended investigation |
| Per-file then cross-file pass | Large code reviews (avoid attention dilution) |
| Map → prioritize → plan | “Add tests to legacy codebase” style work |

## 2.6 Sessions: resume, fork, freshness

- **Named resume:** continue when prior context still mostly valid
- **Fork session:** explore divergent approaches from a shared baseline
- After code changes: **tell the agent what changed** or start fresh with a structured summary — stale tool dumps mislead
- Fresh session + summary often beats resume with rotten tool results

---

# Part 3 - Tool Design & MCP Integration (18%)

## 3.1 Descriptions are the router

LLMs pick tools largely from **names + descriptions**.

Write descriptions that include purpose, inputs/formats, outputs, edge cases, and **when NOT to use** vs similar tools.

**Fix overlap:** rename/split generic analyzers into purpose-specific tools (`extract_web_results`, `summarize_content`, `verify_claim_against_source`).

Watch system prompts for keyword traps that override good descriptions.

## 3.2 Structured tool errors

Return useful failure metadata, not “Operation failed”:

- `errorCategory`: transient / validation / permission / business
- `isRetryable`
- Human-readable message for the agent to relay

Empty successful result ≠ access failure. Subagents should recover locally when possible; escalate partial results upward when stuck.

## 3.3 Tool access & tool_choice

- Too many tools hurts selection — prefer **role-scoped sets**
- Specialists shouldn’t get unrelated tools
- `tool_choice`:
  - `auto` — may answer in text
  - `any` — must call some tool
  - force named tool — must call that tool first

## 3.4 MCP server integration

| Scope | Config | Use |
| --- | --- | --- |
| Project/team | `.mcp.json` | Shared tooling in repo |
| User/personal | `~/.claude.json` | Experiments |

- Expand secrets via `${ENV_VAR}` — don’t commit tokens
- Prefer community MCP servers for standard SaaS; custom for unique internal APIs
- Enrich MCP tool descriptions so agents don’t ignore them for weaker built-ins
- Expose **resources** (catalogs/schemas) to cut exploratory tool spam

## 3.5 Built-in coding tools

| Tool | Use for |
| --- | --- |
| **Grep** | Search file **contents** |
| **Glob** | Find files by **path pattern** |
| **Read** | Load file(s) |
| **Edit** | Targeted change with unique anchors |
| **Write** | Full write / Edit fallback when anchors aren’t unique |
| **Bash** | Shell commands when appropriate |

**Incremental exploration:** Grep entry points → Read imports → trace — don’t dump the whole repo into context.

---

# Part 4 - Claude Code Configuration & Workflows (20%)

## 4.1 CLAUDE.md hierarchy

1. **User:** `~/.claude/CLAUDE.md` — personal only (not shared via git)
2. **Project:** `.claude/CLAUDE.md` or root `CLAUDE.md` — team standards
3. **Directory:** nested `CLAUDE.md` for package-local rules

**Modularize:** `@import` external files; or `.claude/rules/` topic files.

**Diagnose:** new hire missing rules? Instructions were probably user-scoped. Verify which memory files are loaded.

## 4.2 Slash commands & skills

| Artifact | Location | Sharing |
| --- | --- | --- |
| Team command | `.claude/commands/` | Via VCS |
| Personal command | `~/.claude/commands/` | Local |
| Skills | `.claude/skills/*/SKILL.md` | Frontmatter: `context: fork`, `allowed-tools`, `argument-hint` |

- **`context: fork`:** isolate verbose/exploratory skill output from main thread
- **Skills vs CLAUDE.md:** on-demand workflows vs always-on standards

## 4.3 Path-specific rules

`.claude/rules/` + YAML `paths:` globs → load conventions only when editing matching files (e.g. `terraform/**/*`, `**/*.test.tsx`).

## 4.4 Plan mode vs direct execution

| Plan mode | Direct execution |
| --- | --- |
| Large/multi-file, architecture choices, migrations | Small clear fixes, single-function changes |
| Explore safely before committing | Known stack-trace bugfix |

Use an Explore subagent for noisy discovery so the main context stays clean.

## 4.5 Iterative refinement

- Concrete **I/O examples** beat vague prose
- **Tests first**, then feed failures back
- **Interview pattern:** have Claude ask clarifying questions before implementing unfamiliar domains
- Interacting bugs → one rich message; independent bugs → sequential

## 4.6 CI/CD with Claude Code

- Non-interactive: `-p` / `--print` (avoid hanging on stdin)
- Structured: `--output-format json` + `--json-schema` for machine-parseable findings
- Put review/test standards in **project CLAUDE.md**
- **Separate session** for review vs the session that wrote the code
- On re-review: include prior findings; ask for **new/unresolved only**
- Provide existing tests so generation doesn’t duplicate coverage

---

# Part 5 - Prompt Engineering & Structured Output (20%)

## 5.1 Explicit criteria > vibes

Bad: “be conservative”, “only high confidence”.  
Good: categorical rules — report X/Y; skip style nitpicks; severity examples.

High false-positive categories destroy trust — disable/fix them deliberately.

## 5.2 Few-shot prompting

2–4 targeted examples showing desired **format**, ambiguous cases and **why** one choice won, and edge document layouts for extraction.

## 5.3 Structured output

**Most reliable:** tool_use with a JSON schema (forces shape; kills JSON syntax errors).

Still watch **semantic** errors (totals don’t add, wrong field semantics).

| tool_choice | Effect |
| --- | --- |
| auto | Might not call the extraction tool |
| any | Must call a tool |
| force name | Must call the schema tool |

## 5.4 Extraction patterns

- Chunk long docs; carry forward running state carefully
- Validate against schema; retry only retryable failures
- Prefer citations/field provenance for downstream trust

---

# Part 6 - Context Management & Reliability (15%)

## 6.1 Protect the context window

- Summarize verbose tool output before re-injecting
- Isolate exploration in forked/subagent contexts
- Prefer retrieval of needed slices over pasting entire corpora
- Drop stale tool blobs when files changed

## 6.2 Multi-agent provenance

When synthesizing, pass **structured** bundles: claim + source URL/doc/page. Coordinator owns citation integrity.

## 6.3 Escalation & self-checks

- Escalate on policy ambiguity, identity failure, high impact, low confidence after tools
- Self-evaluation: checklist against acceptance criteria before `end_turn`
- Customer-facing language for business errors; don’t loop forever on non-retryable faults

## 6.4 Observability

Route subagent I/O through the coordinator for logs, metrics, and consistent error policy.

---

# Part 7 - Production Scenarios Map

Each exam sitting draws **4 of these 6** frames. Study all.

| # | Scenario | Primary domains |
| --- | --- | --- |
| 1 | **Customer support resolution agent** (MCP tools; FCR target; safe escalation) | 1, 2, 5 |
| 2 | **Code generation with Claude Code** (slash commands, CLAUDE.md, plan vs direct) | 3, 5 |
| 3 | **Multi-agent research system** (coordinator + specialists; citations) | 1, 2, 5 |
| 4 | **Developer productivity agent** (Read/Write/Bash/Grep/Glob + MCP) | 2, 3, 1 |
| 5 | **Claude Code in CI/CD** (reviews, tests, PR feedback; `-p`) | 3, 4 |
| 6 | **Structured data extraction** (JSON schemas, edge cases) | 4, 5 |

**Drill method:** for each scenario, write (1) architecture sketch, (2) tool list + descriptions, (3) hard rules → hooks, (4) context strategy, (5) failure/escalation paths.

---

# Part 8 - Glossary

- **Agent SDK:** Toolkit for building tool-using agents and multi-agent systems.
- **Allowed tools:** Whitelist of tools an agent may call.
- **CLAUDE.md:** Persistent project/user instructions for Claude Code.
- **Coordinator:** Hub agent that delegates and aggregates.
- **Few-shot:** In-prompt examples guiding format/judgment.
- **Fork:** Isolated branch of a session/skill context.
- **Hook:** Deterministic interceptor around tool use.
- **MCP:** Protocol for tools and resources integrated with Claude clients.
- **Plan mode:** Design/explore before applying large changes.
- **stop_reason:** Model signal controlling the agent loop.
- **Structured output:** Schema-constrained model responses.
- **Subagent:** Specialist agent with isolated context.
- **tool_choice:** Policy controlling whether/which tool must be called.

---

# Part 9 - Practice Tests

Original scenario-style items for learning (not exam dumps). Answer first, then expand **Answer**.

## Practice Test 1

1. An agent loop should primarily continue while:
    - A. The assistant message contains the word “continue”
    - B. `stop_reason` is `tool_use`
    - C. Iteration count is under 3
    - D. Any text was produced

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Continue the loop on tool_use; terminate on end_turn. Don’t parse prose or rely on arbitrary caps as the primary stop.
    </details>

2. Subagents in a hub-and-spoke design:
    - A. Automatically inherit the full coordinator transcript
    - B. Need explicit context passed in their prompts
    - C. Share a global mutable memory by default
    - D. Cannot return results to the coordinator

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Subagent context is isolated; pass findings explicitly (ideally structured with provenance).
    </details>

3. Refunds must never run before customer identity is verified. Best enforcement?
    - A. A polite system-prompt reminder only
    - B. Programmatic prerequisite gate / hook blocking process_refund
    - C. Higher temperature
    - D. Disable all logging

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Hard compliance needs deterministic enforcement; prompts alone have non-zero failure rates.
    </details>

4. Heterogeneous MCP tools return Unix times and ISO dates. Best place to normalize?
    - A. PostToolUse hook before the model reasons
    - B. Ask the user to convert dates manually every time
    - C. Ignore timestamps
    - D. Raise temperature

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Hooks normalize tool results deterministically for the model.
    </details>

5. Two tools have near-identical descriptions. Likely symptom?
    - A. Perfect routing forever
    - B. Misrouting / unreliable tool selection
    - C. Faster inference always
    - D. Smaller context windows

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Overlapping descriptions confuse tool choice — split/rename with clear boundaries.
    </details>

6. MCP tool fails with a business rule violation. Response should include:
    - A. Only “Operation failed”
    - B. Structured category, isRetryable=false, clear explanation
    - C. Empty 200 with no body
    - D. Binary stack traces only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Structured errors let the agent choose recovery vs user messaging correctly.
    </details>

7. A synthesis-only subagent is given web search + many unrelated tools. Risk?
    - A. Better specialization
    - B. Misuse of off-role tools and worse selection
    - C. Guaranteed citations
    - D. Free tokens

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Scope tools to the role; too many tools degrade reliability.
    </details>

8. Team-shared MCP servers belong in:
    - A. Only a sticky note
    - B. Project `.mcp.json` (with env var secrets)
    - C. Public gist with tokens
    - D. User config exclusively for all teammates

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Project-scoped MCP config is shared via VCS; keep secrets in env expansion.
    </details>

9. Find all TypeScript test files by name pattern:
    - A. Grep for the string “test”
    - B. Glob `**/*.test.ts`
    - C. Write
    - D. tool_choice any alone

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Glob matches paths; Grep searches contents.
    </details>

10. Edit fails because the anchor text isn’t unique. Fallback?
    - A. Read + Write the file
    - B. Disable the filesystem
    - C. Only raise temperature
    - D. Delete the repo

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: When Edit can’t uniquely match, Read then Write is the reliable path.
    </details>

11. New teammate doesn’t see project coding standards. Likely cause?
    - A. Standards live only in someone’s `~/.claude/CLAUDE.md`
    - B. Too much plan mode
    - C. MCP resources exist
    - D. JSON schemas exist

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: User-level CLAUDE.md isn’t shared via git — put team rules in project config.
    </details>

12. Large CLAUDE.md should be modularized with:
    - A. `@import` / `.claude/rules/` topic files
    - B. Pasting the same blob everywhere
    - C. Removing all standards
    - D. Base64 in filenames

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Modular imports/rules keep context relevant and maintainable.
    </details>

13. Skill produces huge exploratory output. Isolate it with:
    - A. `context: fork` in skill frontmatter
    - B. Higher max tokens only
    - C. Disabling hooks always
    - D. tool_choice auto only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Forked skill context keeps the main conversation clean.
    </details>

14. Microservice restructuring across 40+ files — prefer first:
    - A. Plan mode (then execute)
    - B. Blind direct edit of all files with no plan
    - C. Random destructive shell
    - D. Disable CLAUDE.md

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Plan mode fits architectural, multi-file, multi-approach work.
    </details>

15. Single known null-check bug in one function — prefer:
    - A. Multi-day plan mode ceremony
    - B. Direct execution
    - C. Spawn 12 research subagents
    - D. Force web search

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Small, well-scoped fixes suit direct execution.
    </details>

16. CI must run Claude Code without hanging on prompts:
    - A. Interactive mode only
    - B. Non-interactive `-p` / `--print`
    - C. Remove all flags
    - D. Require a keypress per file

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: `-p` is for headless CI pipelines.
    </details>

17. PR review bot should emit machine-parseable findings:
    - A. Free poetry only
    - B. `--output-format json` with a JSON schema
    - C. Screenshots only
    - D. Unstructured SMS

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Structured CLI output enables automated inline comments.
    </details>

18. Same session that wrote the code now reviews it. Risk?
    - A. Healthier separation of concerns
    - B. Weaker review; prefer an independent session
    - C. Guaranteed security
    - D. Lower false negatives always

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Independent review context is more effective than self-review in the writer session.
    </details>

19. “Only report high-confidence issues” still floods false positives. Better approach?
    - A. Explicit categorical criteria + examples of skip vs report
    - B. Even vaguer wording
    - C. Max temperature
    - D. Remove the schema

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Specific criteria beat confidence vibes for precision.
    </details>

20. Need consistently formatted review comments — strongest lever?
    - A. Few-shot examples of the desired format
    - B. No examples, longer adjectives
    - C. Disable tools
    - D. Rename the model in docs only

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Few-shots anchor format and judgment better than prose alone.
    </details>

21. Guaranteed JSON shape for extraction — most reliable?
    - A. “Please return JSON” in plain text only
    - B. tool_use with a JSON schema (forced as needed)
    - C. Regex on poetry
    - D. CSV in the system prompt title

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Schema via tool_use enforces structure; still validate semantics.
    </details>

22. Schema-valid JSON can still be wrong because:
    - A. Syntax guarantees business truth
    - B. Semantic errors (wrong fields/totals) can remain
    - C. JSON cannot exist
    - D. Hooks forbid JSON

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Structure ≠ correctness — add validation/checks.
    </details>

23. After files changed overnight, resumed session still trusts old Read dumps. Better?
    - A. Blind resume forever
    - B. Inform about changes or start fresh with a structured summary
    - C. Delete MCP
    - D. Disable stop_reason

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Avoid stale tool results; refresh or summarize cleanly.
    </details>

24. Parallel independent research subagents should be spawned:
    - A. One per day only
    - B. Multiple Task calls in one coordinator turn when independent
    - C. Never
    - D. Only via Grep

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Parallel Task emissions in a single turn enable concurrent work.
    </details>

25. Support agent should escalate when:
    - A. Always, even for clear policy password resets
    - B. Policy ambiguity / verification failure / high-impact actions after tools
    - C. Never
    - D. Only when temperature is 0

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Escalate on ambiguity, failed gates, and high-risk actions — with structured handoffs.
    </details>

## Practice Test 2 - Mixed tradeoffs

1. Coordinator prompt should emphasize:
    - A. Rigid 40-step micromanagement only
    - B. Goals + quality criteria so subagents can adapt
    - C. No goals
    - D. Random tools

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Goal/quality-oriented prompts enable adaptable subagents.
    </details>

2. Path-scoped rules help mainly by:
    - A. Loading irrelevant rules always
    - B. Loading conventions only for matching files (saving tokens/noise)
    - C. Deleting MCP
    - D. Forbidding plan mode

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Conditional rules reduce irrelevant context.
    </details>

3. Prefer community MCP server when:
    - A. Integrating a standard system like a common issue tracker
    - B. Secrets must be hardcoded
    - C. Tools shouldn’t have descriptions
    - D. You want no auth ever

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Use community servers for standard integrations; custom for unique internals.
    </details>

4. `tool_choice: "any"` is useful when:
    - A. You want optional chatting with no tools
    - B. You must ensure a tool is called rather than plain text
    - C. You want to ban all tools
    - D. You disable JSON

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: "any" forces a tool call.
    </details>

5. Interview pattern means:
    - A. Claude asks clarifying questions before implementing unfamiliar designs
    - B. Skipping requirements
    - C. Only CI `-p`
    - D. Forking git without prompts

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Surface unknown constraints before coding.
    </details>

6. Re-running CI review after new commits should:
    - A. Repeat every old comment forever
    - B. Include prior findings and report new/still-open issues only
    - C. Delete CLAUDE.md
    - D. Use interactive mode in CI

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Avoid duplicate noise; focus on delta/unresolved.
    </details>

7. MCP resources are valuable because they:
    - A. Hide all catalogs
    - B. Expose content catalogs so agents explore less blindly
    - C. Replace stop_reason
    - D. Disable hooks

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Resources reduce exploratory tool calls.
    </details>

8. Fork session helps when:
    - A. Comparing two approaches from a shared analysis baseline
    - B. Deleting history is mandatory
    - C. Tools must not exist
    - D. CI cannot use JSON

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Fork explores divergent paths from one baseline.
    </details>

9. For extraction edge cases, add:
    - A. Few-shot examples of messy real documents
    - B. No examples
    - C. Only higher temperature
    - D. Fewer schema fields without thought

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: A

      Explanation: Few-shots teach varied layouts and reduce empty/null required fields.
    </details>

10. Observability in multi-agent systems is strongest when:
    - A. Subagents silently peer-to-peer with no hub
    - B. Communication routes through the coordinator
    - C. Logs are forbidden
    - D. Errors are swallowed

    <details markdown=1><summary markdown="span">Answer</summary>
      Correct answer: B

      Explanation: Hub routing centralizes logs, errors, and policy.
    </details>

---

### Quick self-score

| Score (/35) | Result |
| --- | --- |
| 32–35 | Strong tradeoff instincts — keep building labs |
| 24–31 | Solid — drill Domains 1 and 3 misses |
| 16–23 | Re-read Parts 0–4 with hands-on loops |
| Below 16 | Rebuild Part 0 + implement a mini support agent |

## Hands-on lab checklist

1. Build a tiny agent loop printing `stop_reason` each turn
2. Add one MCP tool with rich description + structured errors
3. Gate a dangerous tool behind a hook
4. Create project `CLAUDE.md` + a path-scoped rule + a slash command
5. Run non-interactive Claude Code with JSON schema output
6. Coordinator that spawns two parallel Tasks and synthesizes with citations

---

*Unofficial study notes for personal learning. Verify product flags and certification policies against current Anthropic documentation.*

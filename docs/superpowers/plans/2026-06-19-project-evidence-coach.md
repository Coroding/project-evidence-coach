# Project Evidence Coach Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and validate a reusable `project-evidence-coach` skill that turns authentic project artifacts and a target job description into a persistent, traceable coaching loop with exactly one active next action.

**Architecture:** Keep the trigger and orchestration rules in a concise `SKILL.md`, route detailed behavior into focused references, and persist user-visible state in one Markdown growth record copied from an asset template. Treat examples as behavioral evaluation fixtures: they exercise incomplete project framing, missing research, missing metrics, job mismatch, retrospective-integrity pressure, and second-round reprioritization.

**Tech Stack:** Markdown skill package, YAML agent metadata, Python 3 standard-library contract tests, `skill-creator` initialization and validation scripts.

## Global Constraints

- Coach one project at a time and ship only the AI product manager internship role module in the first release.
- Inspect supplied artifacts before asking questions; disclose selective inspection rather than implying full repository coverage.
- Improve and classify evidence before polishing application prose.
- Keep global visibility but expand exactly one active action; retain only the top three concise priorities.
- Every completed claim must trace to a file, result, link, or explicit user confirmation.
- Classify evidence as existing verified, partial or weak, retrospective validation, or proposed future work.
- Label metrics as suggested metric, instrumented metric, or measured result; never interchange these labels.
- Never fabricate research, ownership, metrics, users, outcomes, historical process, or completed future work.
- Maintain one user-editable file at `project-evidence/PROJECT_GROWTH.md` and preserve user edits.
- Use qualitative maturity states only: missing, initial, presentable, verifiable, application-ready.
- Return five compact sections per round: Round judgment, Diagnostic snapshot, Top three priorities, Active action card, Integrity note.
- Withhold application-specific readiness when the job description is absent; mark the AI product manager baseline as provisional.
- Do not require `saved-to-action`; support only an optional handoff.
- Do not add other role modules, portfolio management, project selection, guarantee language, or a large static roadmap.
- Keep `SKILL.md` under 500 lines and avoid duplicating detailed reference content in it.

## File Structure

```text
.agents/skills/project-evidence-coach/
  SKILL.md                              # Trigger, intake, round loop, routing, output contract
  agents/openai.yaml                    # Skill-list metadata and default invocation prompt
  references/
    core-workflow.md                    # Inspection, parsing, ranking, verification, edge cases
    growth-file-schema.md               # Stable sections, identifiers, merge/update rules
    evidence-integrity.md               # Evidence, timing, ownership, metrics, export gates
    action-card-format.md               # One-action template and reduced-scope rules
    role-modules/ai-product-manager.md  # Eight dimensions and JD-sensitive evaluation
  assets/project-growth-template.md     # Initial PROJECT_GROWTH.md copied into user projects
  examples/
    minimal-vibecoding-project.md       # Missing framing, metrics, and JD-fit evaluation
    project-without-research.md         # Missing users and retrospective-integrity evaluation
    second-round-diagnosis.md           # Artifact verification and dynamic reprioritization
tests/test_skill_contract.py            # Structural and cross-file contract checks
```

---

### Task 1: Establish the Skill Contract and Scaffold

**Files:**
- Create: `.agents/skills/project-evidence-coach/`
- Create: `tests/test_skill_contract.py`
- Create: `.gitignore`

**Interfaces:**
- Consumes: the approved design at `docs/superpowers/specs/2026-06-19-project-evidence-coach-design.md`.
- Produces: a discoverable skill root and a contract-test helper `read(relative: str) -> str` used by every later task.

- [ ] **Step 1: Initialize version control and write the failing contract test**

Run:

```powershell
git init
New-Item -ItemType Directory -Force tests | Out-Null
```

Create `tests/test_skill_contract.py` with:

```python
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "project-evidence-coach"


def read(relative: str) -> str:
    return (SKILL / relative).read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    def test_required_package_files_exist(self):
        required = {
            "SKILL.md",
            "agents/openai.yaml",
            "references/core-workflow.md",
            "references/growth-file-schema.md",
            "references/evidence-integrity.md",
            "references/action-card-format.md",
            "references/role-modules/ai-product-manager.md",
            "assets/project-growth-template.md",
            "examples/minimal-vibecoding-project.md",
            "examples/project-without-research.md",
            "examples/second-round-diagnosis.md",
        }
        self.assertEqual([], sorted(path for path in required if not (SKILL / path).is_file()))

    def test_skill_frontmatter_and_metadata(self):
        skill = read("SKILL.md")
        self.assertTrue(skill.startswith("---\nname: project-evidence-coach\n"))
        description = re.search(r"^description: (.+)$", skill, re.MULTILINE).group(1)
        self.assertTrue(description.startswith("Use when "))
        self.assertLessEqual(len(description), 1024)
        metadata = read("agents/openai.yaml")
        self.assertIn('display_name: "Project Evidence Coach"', metadata)
        self.assertIn("$project-evidence-coach", metadata)

    def test_round_contract_and_single_action_are_explicit(self):
        combined = read("SKILL.md") + read("references/action-card-format.md")
        for heading in (
            "Round judgment",
            "Diagnostic snapshot",
            "Top three priorities",
            "Active action card",
            "Integrity note",
        ):
            self.assertIn(heading, combined)
        self.assertRegex(combined, r"(?i)exactly one active action")

    def test_evidence_and_metric_vocabularies_are_complete(self):
        integrity = read("references/evidence-integrity.md")
        for label in (
            "existing verified evidence",
            "partial or weak evidence",
            "retrospective validation",
            "proposed future work",
            "suggested metric",
            "instrumented metric",
            "measured result",
        ):
            self.assertIn(label, integrity.lower())

    def test_growth_template_has_stable_sections(self):
        template = read("assets/project-growth-template.md")
        for heading in (
            "# Project Growth",
            "## Project and target",
            "## Requirement map",
            "## Evidence ledger",
            "## Current diagnosis",
            "## Priority queue",
            "## Active action card",
            "## Completed actions and output readiness",
        ):
            self.assertIn(heading, template)

    def test_role_module_has_all_eight_dimensions(self):
        role = read("references/role-modules/ai-product-manager.md")
        dimensions = (
            "Problem and context",
            "Users and research",
            "Requirements and prioritization",
            "AI solution fit",
            "Product solution and implementation",
            "Metrics and validation",
            "Iteration and decisions",
            "Outcome and communication",
        )
        self.assertTrue(all(name in role for name in dimensions))

    def test_examples_cover_all_release_scenarios(self):
        examples = "\n".join(
            read(path)
            for path in (
                "examples/minimal-vibecoding-project.md",
                "examples/project-without-research.md",
                "examples/second-round-diagnosis.md",
            )
        )
        for marker in ("SCENARIO-1", "SCENARIO-2", "SCENARIO-3", "SCENARIO-4", "SCENARIO-5", "SCENARIO-6"):
            self.assertIn(marker, examples)

    def test_skill_stays_concise_and_routes_every_reference(self):
        skill = read("SKILL.md")
        self.assertLess(len(skill.splitlines()), 500)
        for path in (
            "references/core-workflow.md",
            "references/growth-file-schema.md",
            "references/evidence-integrity.md",
            "references/action-card-format.md",
            "references/role-modules/ai-product-manager.md",
        ):
            self.assertIn(path, skill)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and confirm the RED state**

Run:

```powershell
python -m unittest tests.test_skill_contract -v
```

Expected: `test_required_package_files_exist` fails and reports the missing package files.

- [ ] **Step 3: Create the skill skeleton with the official initializer**

Run:

```powershell
python "C:\Users\lenovo\.codex\skills\.system\skill-creator\scripts\init_skill.py" project-evidence-coach --path .agents/skills --resources references,assets --interface 'display_name=Project Evidence Coach' --interface 'short_description=Turn project artifacts into traceable job evidence' --interface 'default_prompt=Use $project-evidence-coach to inspect my project against this job description and give me one evidence-building action.'
New-Item -ItemType Directory -Force .agents/skills/project-evidence-coach/references/role-modules | Out-Null
New-Item -ItemType Directory -Force .agents/skills/project-evidence-coach/examples | Out-Null
```

Expected: the initializer creates `SKILL.md`, `agents/openai.yaml`, `references/`, and `assets/` without errors.

- [ ] **Step 4: Add the repository ignore rule and verify the scaffold**

Create `.gitignore` with:

```gitignore
__pycache__/
*.pyc
.worktrees/
```

Run:

```powershell
python -m unittest tests.test_skill_contract.SkillContractTests.test_required_package_files_exist -v
```

Expected: FAIL lists only the resource and example files not yet implemented.

- [ ] **Step 5: Commit the contract and scaffold**

```powershell
git add .gitignore tests .agents/skills/project-evidence-coach/SKILL.md .agents/skills/project-evidence-coach/agents
git commit -m "test: define project evidence coach contract"
```

---

### Task 2: Implement Core Orchestration and Action Contract

**Files:**
- Modify: `.agents/skills/project-evidence-coach/SKILL.md`
- Create: `.agents/skills/project-evidence-coach/references/core-workflow.md`
- Create: `.agents/skills/project-evidence-coach/references/action-card-format.md`

**Interfaces:**
- Consumes: project artifacts, optional job description, deadline, time budget, output goal, constraints, and corrections.
- Produces: `Round judgment`, `Diagnostic snapshot`, `Top three priorities`, `Active action card`, and `Integrity note`, with exactly one expanded action.

- [ ] **Step 1: Add a failing routing assertion**

Add to `SkillContractTests`:

```python
    def test_core_workflow_encodes_priority_order_and_edge_cases(self):
        workflow = read("references/core-workflow.md")
        ordered = (
            "blocking dependency",
            "importance in the target job description",
            "size of the evidence gap",
            "evidence value relative to effort",
            "available time and constraints",
        )
        positions = [workflow.index(item) for item in ordered]
        self.assertEqual(positions, sorted(positions))
        for case in (
            "No job description",
            "Insufficient project material",
            "Large repository",
            "No real users",
            "No historical data",
            "Limited user time",
            "Project/JD mismatch",
            "Unverifiable ownership",
            "Conflicting artifacts",
        ):
            self.assertIn(case, workflow)
```

- [ ] **Step 2: Run the focused test and confirm it fails**

Run:

```powershell
python -m unittest tests.test_skill_contract.SkillContractTests.test_core_workflow_encodes_priority_order_and_edge_cases -v
```

Expected: FAIL because `references/core-workflow.md` does not exist.

- [ ] **Step 3: Replace `SKILL.md` with the concise router**

Write a complete skill file with this structure and wording:

```markdown
---
name: project-evidence-coach
description: Use when a student or early-career candidate has a real but incomplete project and needs artifact-level coaching against a target internship job description, including evidence gaps, truthful validation work, one executable next action, persistent project growth tracking, resume evidence, portfolio cases, or interview stories.
---

# Project Evidence Coach

Inspect authentic project material, compare it with the target job description, and advance the project through one verifiable evidence-building action at a time.

## Start

1. Inspect the supplied project location, artifacts, notes, screenshots, links, and job description before asking questions.
2. State what was inspected and what remains unexamined when coverage is selective.
3. If project material is inaccessible, request the smallest useful evidence set.
4. If the job description is missing, use the AI product manager baseline provisionally and withhold application-specific readiness.
5. Read `references/core-workflow.md` for every coaching round.
6. Read `references/evidence-integrity.md` before classifying or exporting claims.
7. Read `references/growth-file-schema.md` before creating or updating the growth record.
8. Read `references/action-card-format.md` before expanding the top priority.
9. Read `references/role-modules/ai-product-manager.md` when evaluating an AI product manager internship.

## Run a Round

1. Parse and rank job requirements.
2. Collect candidate evidence from inspected artifacts and explicit confirmations.
3. Classify evidence status, timing, confidence, ownership, and metric state.
4. Evaluate the active role dimensions without computing an overall numeric score.
5. Rank the top three gaps using the required priority order.
6. Expand exactly one active action: the first priority.
7. On later rounds, verify the returned artifact before updating evidence or diagnosis.
8. Create or merge `project-evidence/PROJECT_GROWTH.md` without replacing user edits.

## Return

Return these five compact sections in order:

1. **Round judgment** — one sentence naming the most important issue.
2. **Diagnostic snapshot** — maturity by role dimension and evidence changes this round.
3. **Top three priorities** — each gap, value, dependency, and concise ranking reason.
4. **Active action card** — exactly one active action following `references/action-card-format.md`.
5. **Integrity note** — separate existing evidence, retrospective validation, and proposed work.

Never convert proposed work into completed claims, invent historical process, or imply full inspection after selective review.
```

- [ ] **Step 4: Write `core-workflow.md` and `action-card-format.md`**

In `core-workflow.md`, define: intake; selective inspection disclosure; JD normalization; evidence collection; the seven-step coaching loop; the exact priority order; second-round verification; dynamic reprioritization; optional `saved-to-action` handoff; and a table covering all nine named edge cases with required behavior. Define the exact readiness labels `not ready`, `partially usable`, and `application-ready for this JD`, including the warning that readiness neither means universal completeness nor guarantees an employment outcome. Add an evaluation-signals section containing unsupported-claim prevention rate (target 100%), active-action completion rate, percentage of completed actions that add valid evidence, evidence-to-application-artifact conversion rate, user acceptance or edit rate for the proposed next action, and coverage of high-priority job requirements after multiple rounds.

In `action-card-format.md`, define this exact output recipe:

```markdown
## Active action card

- **Objective:** one evidence outcome, not a broad project phase.
- **Why now:** the blocking dependency or high-value requirement this resolves.
- **Steps:** numbered actions that fit the stated time budget.
- **Method or template:** a directly usable procedure, script, question set, or document shape.
- **Acceptance criteria:** observable conditions used in the next round.
- **Artifact to return:** exact file, link, result, screenshot, or explicit confirmation.
- **Supported job requirement:** normalized requirement plus source wording or location.
- **Estimated effort:** realistic range.
- **Reduced-scope version:** smallest version preserving the evidence goal.
```

Also state that only the first of three priorities receives this expansion and that future tasks remain concise queue entries.

- [ ] **Step 5: Run focused orchestration tests**

Run:

```powershell
python -m unittest tests.test_skill_contract.SkillContractTests.test_round_contract_and_single_action_are_explicit tests.test_skill_contract.SkillContractTests.test_core_workflow_encodes_priority_order_and_edge_cases tests.test_skill_contract.SkillContractTests.test_skill_stays_concise_and_routes_every_reference -v
```

Expected: all three focused orchestration tests pass; later tasks add the referenced files required by the full-suite existence check.

- [ ] **Step 6: Commit orchestration**

```powershell
git add .agents/skills/project-evidence-coach/SKILL.md .agents/skills/project-evidence-coach/references/core-workflow.md .agents/skills/project-evidence-coach/references/action-card-format.md tests/test_skill_contract.py
git commit -m "feat: add evidence coaching loop"
```

---

### Task 3: Implement Persistent Growth State

**Files:**
- Create: `.agents/skills/project-evidence-coach/references/growth-file-schema.md`
- Create: `.agents/skills/project-evidence-coach/assets/project-growth-template.md`
- Modify: `tests/test_skill_contract.py`

**Interfaces:**
- Produces: one merge-safe `project-evidence/PROJECT_GROWTH.md` with evidence identifiers `E-001`, requirement identifiers `R-001`, and action identifiers `A-001`.

- [ ] **Step 1: Add a failing merge-safety test**

Add:

```python
    def test_growth_schema_preserves_user_state(self):
        schema = read("references/growth-file-schema.md")
        for rule in (
            "preserve unknown headings",
            "preserve user-authored text",
            "update by stable identifier",
            "never renumber existing identifiers",
            "exactly three priority rows",
            "exactly one active action",
        ):
            self.assertIn(rule, schema.lower())
```

- [ ] **Step 2: Run the test and confirm it fails**

Run: `python -m unittest tests.test_skill_contract.SkillContractTests.test_growth_schema_preserves_user_state -v`

Expected: FAIL because the schema is absent.

- [ ] **Step 3: Write the growth schema**

Define all seven growth-record sections from the design, the three stable identifier formats, allowed evidence timing and maturity values, and these update rules verbatim: preserve unknown headings; preserve user-authored text; update by stable identifier; never renumber existing identifiers; exactly three priority rows unless fewer than three meaningful gaps exist; exactly one active action; append only concise completed-action deltas; ask before resolving contradictory user edits.

Include Markdown table schemas for requirements and evidence. The evidence columns must be: ID, supported claim or capability, source, temporal status, confidence, unresolved questions, supported outputs, linked requirements.

- [ ] **Step 4: Write the project growth asset**

Create the seven required headings and empty tables with instructional HTML comments. Use `Not provided` for missing target/deadline fields, `No evidence recorded yet` for an empty ledger, `No action selected yet` for the active action, and no fabricated sample accomplishments.

- [ ] **Step 5: Run growth-state tests**

Run:

```powershell
python -m unittest tests.test_skill_contract.SkillContractTests.test_growth_template_has_stable_sections tests.test_skill_contract.SkillContractTests.test_growth_schema_preserves_user_state -v
```

Expected: PASS.

- [ ] **Step 6: Commit persistent state**

```powershell
git add .agents/skills/project-evidence-coach/references/growth-file-schema.md .agents/skills/project-evidence-coach/assets/project-growth-template.md tests/test_skill_contract.py
git commit -m "feat: add persistent project growth record"
```

---

### Task 4: Implement Evidence Integrity and Export Gates

**Files:**
- Create: `.agents/skills/project-evidence-coach/references/evidence-integrity.md`
- Modify: `tests/test_skill_contract.py`

**Interfaces:**
- Produces: a classification decision for every observation and an export gate that blocks unsupported resume, portfolio, and interview claims.

- [ ] **Step 1: Add a failing integrity-gate test**

Add:

```python
    def test_integrity_reference_blocks_unsupported_exports(self):
        integrity = read("references/evidence-integrity.md").lower()
        for phrase in (
            "do not export",
            "explicit user confirmation",
            "truthful timing",
            "ownership blocked",
            "conflicting artifacts",
            "resume",
            "portfolio",
            "interview",
        ):
            self.assertIn(phrase, integrity)
```

- [ ] **Step 2: Run the integrity tests and confirm failure**

Run: `python -m unittest tests.test_skill_contract.SkillContractTests.test_evidence_and_metric_vocabularies_are_complete tests.test_skill_contract.SkillContractTests.test_integrity_reference_blocks_unsupported_exports -v`

Expected: both tests fail because the reference is absent.

- [ ] **Step 3: Write the evidence-integrity reference**

Define the four evidence states with upgrade conditions, original/retrospective/proposed timing, confidence as high/medium/low, ownership confirmation, conflict handling, and the three metric labels. Add an export matrix: existing verified evidence may export when ownership and source are clear; partial evidence does not export as a completed claim; retrospective validation may export only with truthful timing; proposed future work does not export.

Add a mandatory pre-export check requiring a source, timing label, ownership status, confidence, linked requirement, and supported output for each claim. Use the exact phrase `do not export` for failed checks, `ownership blocked` for unresolved contribution, and require resolution before using `conflicting artifacts`.

- [ ] **Step 4: Run the integrity tests**

Run the command from Step 2 again.

Expected: PASS.

- [ ] **Step 5: Commit integrity rules**

```powershell
git add .agents/skills/project-evidence-coach/references/evidence-integrity.md tests/test_skill_contract.py
git commit -m "feat: enforce evidence integrity gates"
```

---

### Task 5: Implement the AI Product Manager Role Module

**Files:**
- Create: `.agents/skills/project-evidence-coach/references/role-modules/ai-product-manager.md`
- Modify: `tests/test_skill_contract.py`

**Interfaces:**
- Consumes: normalized JD requirements and classified evidence.
- Produces: one maturity state per dimension plus requirement-sensitive gap candidates; no equal weighting and no overall numeric score.

- [ ] **Step 1: Add a failing qualitative-evaluation test**

Add:

```python
    def test_role_module_is_jd_sensitive_and_non_numeric(self):
        role = read("references/role-modules/ai-product-manager.md").lower()
        for maturity in ("missing", "initial", "presentable", "verifiable", "application-ready"):
            self.assertIn(maturity, role)
        self.assertIn("job description changes", role)
        self.assertIn("not equally weighted", role)
        self.assertNotRegex(role, r"\b\d{1,3}/100\b")
```

- [ ] **Step 2: Run role-module tests and confirm failure**

Run: `python -m unittest tests.test_skill_contract.SkillContractTests.test_role_module_has_all_eight_dimensions tests.test_skill_contract.SkillContractTests.test_role_module_is_jd_sensitive_and_non_numeric -v`

Expected: FAIL because the role module is absent.

- [ ] **Step 3: Write the role module**

For each of the eight dimensions, include: diagnostic question; acceptable artifact types; weak-evidence warning; and maturity anchors from missing through application-ready. State that `job description changes` alter relative priority, dimensions are `not equally weighted`, and a project need not cover every dimension when another project should support a requirement.

For Metrics and validation, explicitly cover product value, AI quality, failure cases, latency, and cost when relevant. For AI solution fit, require why AI is appropriate plus model/data/prompt/workflow choices, limitations, and risks. For Product solution and implementation, separate working artifact evidence from contribution/ownership evidence.

- [ ] **Step 4: Run role-module tests**

Run the command from Step 2 again.

Expected: PASS.

- [ ] **Step 5: Commit the role module**

```powershell
git add .agents/skills/project-evidence-coach/references/role-modules/ai-product-manager.md tests/test_skill_contract.py
git commit -m "feat: add ai product manager evaluation module"
```

---

### Task 6: Add Behavioral Evaluation Fixtures

**Files:**
- Create: `.agents/skills/project-evidence-coach/examples/minimal-vibecoding-project.md`
- Create: `.agents/skills/project-evidence-coach/examples/project-without-research.md`
- Create: `.agents/skills/project-evidence-coach/examples/second-round-diagnosis.md`
- Modify: `tests/test_skill_contract.py`

**Interfaces:**
- Produces: reproducible prompts, fixture facts, prohibited inferences, and observable pass criteria for all six release scenarios.

- [ ] **Step 1: Add a failing fixture-shape test**

Add:

```python
    def test_each_example_defines_behavioral_oracle(self):
        for path in (
            "examples/minimal-vibecoding-project.md",
            "examples/project-without-research.md",
            "examples/second-round-diagnosis.md",
        ):
            example = read(path)
            for heading in ("## Fixture", "## Prompt", "## Must observe", "## Must not infer"):
                self.assertIn(heading, example)
```

- [ ] **Step 2: Run example tests and confirm failure**

Run: `python -m unittest tests.test_skill_contract.SkillContractTests.test_examples_cover_all_release_scenarios tests.test_skill_contract.SkillContractTests.test_each_example_defines_behavioral_oracle -v`

Expected: FAIL because the examples are absent.

- [ ] **Step 3: Write the minimal-vibecoding fixture**

Cover `SCENARIO-1`, `SCENARIO-3`, and `SCENARIO-4`. Supply facts for a working demo with source files but no README, framing, analytics, or measured outcomes, plus an AI PM JD emphasizing research and metrics. Require artifact citations, truthful missing states, top-three ranking, exactly one expanded action, and an explicit note that some JD requirements may belong to another project.

- [ ] **Step 4: Write the no-research fixture**

Cover `SCENARIO-2` and `SCENARIO-5`. Supply a working product with no authentic user research and a user request to phrase a newly planned interview as if it happened during original development. Require refusal to rewrite history, classification as proposed work before execution and retrospective validation afterward, and a reduced-scope research action.

- [ ] **Step 5: Write the second-round fixture**

Cover `SCENARIO-6`. Provide round-one state, a returned usability-test artifact, and a changed JD. Require source verification before ledger update, preservation of user-authored growth-file text, a concise completed-action delta, diagnosis change, dynamic reprioritization, and exactly one new active action.

- [ ] **Step 6: Run all example tests**

Run the command from Step 2 again.

Expected: PASS.

- [ ] **Step 7: Commit evaluation fixtures**

```powershell
git add .agents/skills/project-evidence-coach/examples tests/test_skill_contract.py
git commit -m "test: add project coaching behavior fixtures"
```

---

### Task 7: Validate Metadata, Package Structure, and Full Contract

**Files:**
- Modify: `.agents/skills/project-evidence-coach/agents/openai.yaml`
- Modify: any skill file that fails validation

**Interfaces:**
- Produces: a structurally valid, discoverable skill package with all deterministic tests passing.

- [ ] **Step 1: Regenerate deterministic metadata from the finished skill**

Run:

```powershell
python "C:\Users\lenovo\.codex\skills\.system\skill-creator\scripts\generate_openai_yaml.py" .agents/skills/project-evidence-coach --interface 'display_name=Project Evidence Coach' --interface 'short_description=Turn project artifacts into traceable job evidence' --interface 'default_prompt=Use $project-evidence-coach to inspect my project against this job description and give me one evidence-building action.'
```

Expected: `agents/openai.yaml` contains only quoted interface strings and no unrequested icon, color, dependency, or policy fields.

- [ ] **Step 2: Run the official package validator**

Run:

```powershell
python "C:\Users\lenovo\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .agents/skills/project-evidence-coach
```

Expected: validator reports the skill is valid.

- [ ] **Step 3: Run the complete deterministic test suite**

Run:

```powershell
python -m unittest discover -s tests -v
```

Expected: all tests pass with zero failures and zero errors.

- [ ] **Step 4: Check concision and unresolved authoring markers**

Run:

```powershell
(Get-Content .agents/skills/project-evidence-coach/SKILL.md).Count
$markers = @('T' + 'ODO', 'T' + 'BD', 'implement' + ' later', 'fill in' + ' details')
rg -n ($markers -join '|') .agents/skills/project-evidence-coach
```

Expected: line count is below 500; `rg` returns no matches.

- [ ] **Step 5: Commit validated metadata**

```powershell
git add .agents/skills/project-evidence-coach
git commit -m "chore: validate project evidence coach package"
```

---

### Task 8: Run Forward Behavioral Validation

**Files:**
- Modify: skill files only when an observed behavior contradicts a fixture oracle
- Create: `.agents/skills/project-evidence-coach/examples/validation-results.md`

**Interfaces:**
- Consumes: the three fixture prompts and finished skill package.
- Produces: baseline and skill-enabled observations for all six scenarios, with every oracle item marked pass or fail.

- [ ] **Step 1: Run RED baseline evaluations in fresh contexts**

Use a fresh agent context for each example with the project skill excluded. Submit only the text under `## Fixture` and `## Prompt`. Record the response and score every `## Must observe` and `## Must not infer` item in `examples/validation-results.md` under `Baseline`.

Expected: at least one baseline misses an oracle item; record the exact miss instead of inventing a failure.

- [ ] **Step 2: Run GREEN evaluations with the skill enabled**

Repeat each prompt in a fresh context with `$project-evidence-coach` explicitly invoked. Record results under `Skill enabled` using the same oracle checklist.

Expected: all oracle items pass, every output has five sections, only one action is expanded, and unsupported claims remain blocked.

- [ ] **Step 3: Correct only observed gaps and re-run affected fixtures**

If a fixture fails, change the smallest relevant instruction or reference rule, record the observed failure and correction, then repeat that fixture in a new context. Do not add speculative guidance unrelated to a recorded failure.

Expected: every affected fixture passes after correction.

- [ ] **Step 4: Re-run static validation after behavioral corrections**

Run:

```powershell
python -m unittest discover -s tests -v
python "C:\Users\lenovo\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .agents/skills/project-evidence-coach
```

Expected: all contract tests pass and the package validator reports valid.

- [ ] **Step 5: Commit behavioral validation**

```powershell
git add .agents/skills/project-evidence-coach tests
git commit -m "test: verify project evidence coach behavior"
```

## Final Verification

- [ ] Confirm every design section maps to at least one task or global constraint.
- [ ] Confirm no package file contains unresolved authoring markers.
- [ ] Confirm identifiers, maturity states, evidence states, metric labels, readiness labels, and output headings are consistent across all files.
- [ ] Confirm `git status --short` is clean.
- [ ] Use `requesting-code-review` for a whole-branch review, then `finishing-a-development-branch` for the integration choice.

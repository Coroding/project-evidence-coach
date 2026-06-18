# Project Evidence Coach Design

## 1. Purpose

`project-evidence-coach` is a persistent project-development coach for students and early-career candidates who have a real but incomplete project and want to make it useful for a target internship.

The skill reads the candidate's existing artifacts, compares them with a target job description, identifies the most valuable evidence gap, and recommends one executable next action. After the user completes that action, the skill verifies the new artifact, updates the project's growth record, and chooses the next action.

The skill does not merely rewrite resume bullets. Its final output is a traceable project evidence package that can support:

- concise resume bullets;
- a complete portfolio case;
- defensible interview stories;
- the underlying files, records, and user confirmations that support those claims.

## 2. Product Scope

### 2.1 Initial scope

The first release coaches one project at a time. It uses a general requirement-to-evidence engine and ships with one role module: AI product manager internships.

The architecture permits additional role modules later, such as frontend engineering, product design, data analysis, or operations. Those modules are outside the first release.

### 2.2 Relationship to Saved-to-Action

`saved-to-action` and `project-evidence-coach` remain separate skills with an optional handoff:

- `saved-to-action` converts scattered job-search material into priorities and may identify which project is worth improving.
- `project-evidence-coach` performs sustained, artifact-level coaching for the selected project.

Each skill must also work independently. The project coach does not require the user to run `saved-to-action` first.

### 2.3 Non-goals

The first release will not:

- manage the candidate's entire application portfolio;
- choose among several projects;
- guarantee interviews or offers;
- fabricate research, ownership, metrics, users, or outcomes;
- turn future work into completed experience;
- require every project to demonstrate every target-role capability;
- expand all suggested tasks into a large static roadmap.

## 3. Core Design Principles

1. **Inspect before asking.** Read the supplied repository, files, screenshots, links, notes, and job description before requesting information the user may already have provided.
2. **Evidence before prose.** Improve the project evidence before polishing claims about it.
3. **One active task.** Maintain global visibility but expand only the highest-priority next action.
4. **Traceable claims.** Every completed claim must point to a file, result, link, or explicit user confirmation.
5. **Time-aware integrity.** Distinguish work performed during original development from later validation and future recommendations.
6. **Role relevance over generic completeness.** Prioritize evidence that matters to the current job description.
7. **Persistent, editable state.** Keep a project-local growth record that the user can inspect and edit.

## 4. Inputs and Intake

### 4.1 Required inputs

The preferred starting inputs are:

- a project location or a collection of project artifacts;
- a target job description.

If the job description is absent, the skill may perform a provisional diagnosis using the AI product manager role baseline. It must label the assumption and request a real job description before making application-specific readiness claims.

If project artifacts are absent or inaccessible, the skill must request the smallest useful evidence set rather than infer project quality from a title or summary.

### 4.2 Optional inputs

- application deadline;
- time available for the current action;
- intended output, such as resume, portfolio, or interview preparation;
- candidate constraints and privacy requirements;
- explicit user corrections or confirmations.

### 4.3 Inspection behavior

For a large repository, inspect entry documentation, top-level structure, executable product surfaces, and files that are directly relevant to the diagnosis. State which areas were inspected and which remain unexamined. Do not imply full coverage after a partial inspection.

Ask follow-up questions only when the missing answer would materially change the diagnosis or the next action.

## 5. Core Coaching Loop

Each coaching round follows this sequence:

1. Parse the target job description and extract high-value requirements.
2. Inspect current project artifacts and collect candidate evidence.
3. Classify evidence by status and confidence.
4. Evaluate the project using the active role module.
5. Identify and rank the three most important evidence gaps.
6. Expand only the first gap into an executable action card.
7. On the next round, verify the submitted artifact, update the growth record, and recalculate the priorities.

Priority is determined in this order:

1. blocking dependency;
2. importance in the target job description;
3. size of the evidence gap;
4. evidence value relative to effort;
5. the user's available time and constraints.

The queue is dynamic. Completing one task can change or remove later tasks.

## 6. Evidence Model and Integrity Rules

Every relevant observation belongs to one of four states:

### 6.1 Existing verified evidence

The artifact or result exists and can be inspected or explicitly confirmed. It may support a current application claim.

### 6.2 Partial or weak evidence

There are signs that the work occurred, but ownership, method, result, or traceability is incomplete. It cannot be upgraded silently.

### 6.3 Retrospective validation

The user performs valid work after the initial build, such as usability testing, follow-up interviews, evaluation, analytics setup, or decision reconstruction from authentic records. It may strengthen the project, but must be described with truthful timing.

### 6.4 Proposed future work

The work has not yet been performed. It may appear in an action card, but never in a resume claim or completed evidence export.

The skill may organize authentic historical decisions from commits, notes, conversations, or user confirmation. It may not invent a plausible product process and present it as history.

Metrics must be labeled as one of:

- suggested metric;
- instrumented metric;
- measured result.

These labels are not interchangeable.

## 7. Persistent Project Growth Record

The first release maintains one user-editable Markdown file:

`project-evidence/PROJECT_GROWTH.md`

A single file keeps the initial workflow portable and easy to inspect. It can be split in a later version if real usage shows that it becomes unwieldy.

The file contains:

### 7.1 Project and target

- project name and current stage;
- target role and job-description source;
- deadline, available time, and constraints.

### 7.2 Requirement map

For each important requirement:

- normalized requirement;
- source wording or location;
- importance;
- current support status;
- relevant evidence identifiers.

### 7.3 Evidence ledger

For each evidence item:

- stable identifier;
- supported claim or capability;
- source file, link, result, or user confirmation;
- temporal status: original, retrospective, or proposed;
- confidence and unresolved questions;
- supported outputs: resume, portfolio, interview;
- linked job requirements.

### 7.4 Current diagnosis

Each role dimension uses qualitative maturity states:

- missing;
- initial;
- presentable;
- verifiable;
- application-ready.

The skill does not use pseudo-precise overall scores such as 82/100.

### 7.5 Priority queue

Keep the current top three gaps with concise ranking reasons and dependencies.

### 7.6 Active action card

Store exactly one expanded task, its acceptance criteria, expected artifact, and time budget.

### 7.7 Completed actions and output readiness

Record concise changes:

- completed action;
- evidence added or changed;
- diagnosis change;
- application outputs now supported.

The record must preserve user edits and must not become an exhaustive activity log.

## 8. AI Product Manager Role Module

The initial role module evaluates eight dimensions:

1. **Problem and context:** target user, problem, scenario, and reason the problem matters.
2. **Users and research:** target-user definition, methods, raw feedback, and traceable insights.
3. **Requirements and prioritization:** requirement origin, prioritization logic, trade-offs, and rejected scope.
4. **AI solution fit:** why AI is appropriate, model/data/prompt/workflow choices, limitations, and risks.
5. **Product solution and implementation:** working artifact, critical flow, prototype or code, and the candidate's actual contribution.
6. **Metrics and validation:** product-value metrics and AI-quality measures, including failure cases, latency, and cost where relevant.
7. **Iteration and decisions:** feedback, observed problems, changes, and the evidence behind each decision.
8. **Outcome and communication:** verified results and their conversion into resume, portfolio, and interview material.

The dimensions are not equally weighted. The target job description changes their relative priority. A project also does not need to cover every dimension if its evidence role in the candidate's broader portfolio is clear.

## 9. Round Output Contract

Each round returns five compact sections.

### 9.1 Round judgment

One sentence naming the project's most important current issue.

### 9.2 Diagnostic snapshot

Show maturity by role dimension and identify evidence added, removed, weakened, or strengthened during the round.

### 9.3 Top three priorities

For each priority, show the gap, value, and dependency. Do not expand all three into detailed plans.

### 9.4 Active action card

The first priority is expanded with:

- objective;
- why it should happen now;
- concrete steps;
- method or template;
- acceptance criteria;
- artifact to return for verification;
- supported job requirement;
- estimated effort;
- reduced-scope version for limited time.

### 9.5 Integrity note

State which elements are existing evidence, retrospective validation, and proposed work.

## 10. Error and Edge-Case Handling

- **No job description:** use a labeled provisional role baseline and withhold application-specific readiness.
- **Insufficient project material:** create a minimum evidence-collection task rather than invent details.
- **Large repository:** inspect selectively, disclose inspection scope, and request only relevant additional paths.
- **No real users:** recommend the smallest suitable interview, usability test, survey, or behavioral validation task.
- **No historical data:** separate suggested, instrumented, and measured metrics.
- **Limited user time:** preserve the evidence goal while reducing sample size or artifact scope.
- **Project/JD mismatch:** say which requirement should be supported by another project instead of forcing artificial completeness.
- **Unverifiable ownership:** request confirmation or mark the claim as blocked.
- **Conflicting artifacts:** surface the conflict and ask for resolution before exporting the affected claim.

## 11. Readiness and Graduation

The project may be labeled:

- **not ready:** one or more blocking requirements lack usable evidence;
- **partially usable:** some truthful outputs are ready, but important gaps remain;
- **application-ready for this JD:** high-priority requirements are supported by credible evidence and every exported claim is traceable.

Application-ready does not mean the project is universally complete or that it guarantees an employment outcome.

The evidence package should be able to produce:

- verified resume bullet inputs;
- a portfolio case outline with linked artifacts;
- one or more interview stories with defensible details;
- a list of remaining limitations and truthful caveats.

## 12. Proposed Skill Structure

```text
.agents/skills/project-evidence-coach/
  SKILL.md
  references/
    core-workflow.md
    growth-file-schema.md
    evidence-integrity.md
    action-card-format.md
    role-modules/
      ai-product-manager.md
  assets/
    project-growth-template.md
  examples/
    minimal-vibecoding-project.md
    project-without-research.md
    second-round-diagnosis.md
```

`SKILL.md` owns triggers, the main loop, and reference routing. Role-specific rules remain isolated in role modules. Templates define stable user-facing artifacts. Examples serve as evaluation fixtures.

## 13. Verification Strategy

The first release must cover these scenarios:

1. code exists, but README and product framing are absent;
2. a working product exists, but user research is absent;
3. research and functionality exist, but metrics or results are absent;
4. the project is credible but poorly matched to the target job description;
5. the user attempts to present retrospective work as original history;
6. the user completes an action card and returns for a second diagnosis.

Each scenario verifies that the skill:

- cites real artifacts instead of fabricating evidence;
- classifies evidence timing correctly;
- ranks three gaps and expands only one;
- provides concrete steps, an artifact, and acceptance criteria;
- changes priorities when the target job description changes;
- preserves history and updates diagnosis after new evidence appears.

## 14. Product Success Measures

- unsupported-claim prevention rate, with a target of 100%;
- active-action completion rate;
- percentage of completed actions that add valid evidence;
- evidence-to-application-artifact conversion rate;
- user acceptance or edit rate for the proposed next action;
- coverage of high-priority job requirements after multiple rounds.

The strongest success signal is not report length. It is the completion of a truthful, useful artifact that strengthens the project's application evidence.


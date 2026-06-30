---
name: project-evidence-coach
description: Use when a student or early-career candidate has a real GitHub/repo/project and wants artifact-grounded materials for product manager, AI product manager, To C PM internships, vibe-coded PM cases, portfolio case studies, interview stories, or resume bullets without inventing evidence.
---

# Project Evidence Coach

Inspect authentic project material, separate verified evidence from gaps, and turn one real project into PM-facing resume, portfolio, and interview artifacts without overstating what the sources prove.

## Start

1. Inspect the supplied project location, GitHub URL, repo URL, local path, ZIP, artifacts, notes, screenshots, links, job description, and intended output goal before asking questions.
2. If the user gives a GitHub/repo/project URL or asks to turn a project into resume bullets, a PM case, a product manager portfolio case, interview stories, or a vibe-coded project case, enter **repository-to-resume-package mode**.
3. Treat the target project repository as a read-only input source. Do not edit its README, source code, docs, deployment config, issues, branches, commits, or pull requests unless the user explicitly changes the task.
4. Write outputs only to `career-case-package/<project-slug>/` in the current workspace. `PROJECT_GROWTH.md` is one package file, not the only deliverable.
5. Read `references/core-workflow.md` for every coaching round.
6. Read `references/evidence-integrity.md` before classifying or exporting claims.
7. Read `references/growth-file-schema.md` before creating or updating a growth record.
8. Read `references/action-card-format.md` before expanding the top priority.
9. Read `references/repository-to-resume-workflow.md` when repository-to-resume-package mode is active.
10. Read `references/package-output-contract.md` before generating package files.
11. Read `references/case-readiness-scoring.md` before writing `02_CASE_READINESS_SCORECARD.md`.
12. Read `references/product-decision-log.md` before writing `04_PRODUCT_DECISION_LOG.md`.
13. Read `references/role-modules/ai-product-manager.md` when evaluating an AI product manager internship or when no JD is supplied and the user targets product/AI product roles.

## Repository-To-Resume-Package Mode

Use this mode when the user supplies a GitHub URL, repo URL, project library/address, local repository, ZIP, pasted README/docs, screenshots, demo link, or asks for a resume package, PM case, product manager portfolio case, interview preparation, or resume bullets from a project.

Each generated package includes an Ownership and Source Appendix so first-person resume claims are separated from repository-visible facts.

Required workflow:

1. **Source inspection** - resolve the strongest available source tier and record inspected/unexamined sources.
2. **Evidence ledger** - classify every key claim with evidence state, temporal status, ownership status, confidence, metric label, source, and missing evidence.
3. **Case readiness scoring** - produce a transparent case-usability scorecard for resume, portfolio, and interview readiness. This scorecard is an evidence-completeness aid, not a hiring prediction.
4. **PM case package generation** - create the full package in `career-case-package/<project-slug>/` even when inspection is limited.
5. **Resume/export boundary check** - mark each claim as 可直接使用, 确认个人贡献后可使用, 仅可带 caveat 使用, or 补证据前禁用.
6. **Next evidence action** - place missing materials in the backlog, missing source checklist, and active action card.

Fallback inspection ladder:

- **Full inspection:** local repository, user-provided ZIP, or successful clone.
- **Limited inspection:** clone fails, but GitHub page, rendered README, visible directory structure, demo link, deployment link, repo metadata, or raw README is visible.
- **User-supplied inspection:** user pasted README, docs, screenshot descriptions, demo links, feature notes, or an evidence table.
- **Source-blocked:** no repository page, README, project description, file list, demo/deployment link, screenshot, or pasted material is accessible.

Clone failure is not fatal if repository web page or README-visible metadata is available. In **limited-inspection package mode**, still generate the complete package and label every file with `inspection_level: limited-inspection`, evidence state, confidence, and missing evidence. Only stop case-body generation in source-blocked mode, and then output the smallest material checklist needed to resume.

## Run A Coaching Round

1. Parse and rank job requirements. If there is no job description, use the AI product manager baseline provisionally and withhold application-specific readiness.
2. Collect candidate evidence from inspected artifacts and explicit confirmations.
3. Classify evidence status, timing, confidence, ownership, and metric state.
4. Evaluate active role dimensions using allowed qualitative maturity states.
5. In repository-to-resume-package mode, generate or update the package files required by `references/package-output-contract.md`.
6. Rank the top three gaps using the required priority order.
7. Expand exactly one active action: the first priority.
8. On later rounds, verify the returned artifact before updating evidence, diagnosis, scores, or export eligibility.

## Return

For ordinary coaching rounds, return these five compact sections in order:

1. **Round judgment** — one sentence naming the most important issue.
2. **Diagnostic snapshot** — maturity by role dimension and evidence changes this round.
3. **Top three priorities** — each gap, value, dependency, and concise ranking reason.
4. **Active action card** — exactly one active action that explicitly includes objective, why now, concrete steps, method or template, acceptance criteria, artifact to return, supported job requirement, estimated effort, and reduced-scope version.
5. **Integrity note** — separate existing evidence, retrospective validation, and proposed work; whenever an active action is still uncompleted, state that it remains proposed future work, and if performed after the original build, it becomes retrospective validation only after the returned artifact is inspected and verified.

For repository-to-resume-package mode, return:

1. **Package created** - output directory and inspection level.
2. **What was inspected** - source tier, sources used, and unexamined sources.
3. **Case readiness scorecard** - resume, portfolio, and interview usability plus main blockers.
4. **Export boundary** - what can be used now, what requires ownership confirmation or caveats, and what is 补证据前禁用.
5. **Next evidence action** - exactly one active action and the missing source checklist location.

Never convert proposed work into completed claims, invent historical process, invent users, interviews, surveys, metrics, launch results, growth numbers, retention, conversion, revenue, AI quality gains, or model performance. Missing material belongs in backlog, missing source checklist, and the action card; it must not be the only result when limited inspection is possible.

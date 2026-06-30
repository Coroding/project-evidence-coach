# Repository to Resume Workflow

Use this reference when a user wants to turn a real GitHub repository, repo URL, local project, ZIP, README, demo, or pasted project material into product manager resume, portfolio, or interview artifacts.

## Applicable scenarios

- The user provides a GitHub URL, repo URL, project library/address, local repository, or ZIP.
- The user asks for resume bullets, a product manager case, AI product manager case, To C PM internship material, portfolio case study, or interview stories.
- The user says a vibe-coded or engineering-heavy project needs to be packaged as a PM case.
- The user asks to analyze an existing project without modifying the source repository.

## Input types

- Local repository path.
- User-provided ZIP or copied project folder.
- Public GitHub repository URL.
- GitHub rendered README or raw README URL.
- Visible file tree, repo metadata, language breakdown, release/deployment links, GitHub Pages link, Vercel/Netlify/Fly/Render links, screenshots, or demo URLs.
- Pasted README, docs, screenshot descriptions, feature notes, project notes, or evidence tables.

## Trigger conditions

Enter `repository-to-resume-package mode` when any of these are present:

- A GitHub/repo/project URL plus a PM, internship, resume, portfolio, or interview goal.
- Phrases such as "project to resume package", "PM case", "product manager portfolio", "interview story", "resume bullet", "AI PM internship", "To C PM internship", or "vibe-coded project".
- A request to analyze a project library/repository as career evidence.

## Repository inspection checklist

Record inspected and unexamined sources explicitly.

- Repository identity: name, owner, URL, visibility, project slug.
- README: product description, user/problem language, feature list, setup, demo links, screenshots, limitations.
- File tree: app structure, frontend/backend/mobile/AI/data/config hints.
- Docs: PRD, notes, architecture, prompts, evals, user flows, roadmap, decisions, screenshots.
- Deployment/demo: GitHub Pages, Vercel, Netlify, app store, video, live demo, docs site.
- Source signals: feature names, route names, UI components, API endpoints, model calls, prompt templates, analytics or logging.
- Collaboration and ownership: commits, PRs, issues, contributors, explicit user confirmation.
- Validation signals: tests, eval logs, feedback, benchmark scripts, analytics, issue comments, bug reports.
- PM artifacts: requirements, prioritization, tradeoffs, scope cuts, iteration history, risk notes.

Do not claim full inspection unless the relevant files were actually read.

## GitHub project to PM-career translation

Translate engineering artifacts into PM language only when the source supports the claim:

- README problem framing -> product context, target scenario, first portfolio section.
- Feature list or UI routes -> user flow and product scope.
- File tree and source names -> implementation capability and likely product surface, with confidence labels.
- Prompt/model/API code -> AI workflow, constraints, risk, and evaluation needs.
- Issues/commits/roadmap -> prioritization, iteration, and decisions.
- Demo/screenshots -> user journey evidence and portfolio visuals.
- Tests/evals/logs/feedback -> validation evidence.

When the source only suggests a claim, label it `partial or weak evidence` and keep the wording qualified. Do not convert source hints into finished PM accomplishments.

## Read-only boundary

The target repository is an input source, not an output location.

- Do not edit README, docs, source code, package files, deployment config, issues, branches, commits, PRs, or releases in the target project.
- Do not push or open PRs against the target project.
- Do not create files inside the target repository unless the user explicitly changes the task.
- Write all career materials to `career-case-package/<project-slug>/` in the current workspace using the standard numbered filenames from `package-output-contract.md`.

## Fallback inspection ladder

Use the strongest available tier, but continue downward before stopping:

```text
1. Local repository or user-provided ZIP
2. Direct git clone
3. GitHub web page / README-rendered page
4. raw README URL
5. visible file tree and demo/deployment links
6. user-provided pasted materials
```

Inspection states:

- **full-inspection:** local repo, ZIP, or clone is available and relevant files were read.
- **limited-inspection:** clone failed, but GitHub page, rendered README, raw README, visible file tree, repo metadata, demo link, or deployment link is available.
- **user-supplied-inspection:** user-pasted README/docs/screenshots/links/notes are the inspectable source.
- **source-blocked:** none of the above exists or can be accessed.

Clone failure is not fatal if repository web page or README-visible metadata is available. In `limited-inspection package mode`, generate the full package anyway and label every file with `inspection_level: limited-inspection`, evidence states, confidence, and missing evidence.

Only stop generating case-body files in `source-blocked` mode. In source-blocked mode, output the smallest useful material checklist and do not fabricate a case narrative.

## Limited-inspection package mode

When only partial GitHub/web/README metadata is available:

1. Create `career-case-package/<project-slug>/`.
2. Generate every required package file from `package-output-contract.md`, including `04_PRODUCT_DECISION_LOG.md`, `06_RESUME_BULLETS_CN.md`, `07_PORTFOLIO_CASE_STUDY_CN.md`, `08_INTERVIEW_STORIES_CN.md`, and `12_OWNERSHIP_AND_SOURCE_APPENDIX.md`.
3. Mark unsupported sections as `insufficient evidence`, not blank.
4. Put requested materials in `10_MISSING_SOURCE_CHECKLIST.md`, backlog, and the active action card.
5. Keep resume bullets conservative or blocked if ownership, problem, impact, or metrics are not verified.
6. State what can be used now: usually project title, conservative project description, cautious interview framing, and next-validation plan.
7. If ownership is not confirmed, generate `12_OWNERSHIP_AND_SOURCE_APPENDIX.md` as a pending user-confirmation template.

## Source-blocked behavior

Use source-blocked only when no repository page, README, file list, demo/deployment link, screenshot, pasted content, or project description is accessible.

Return:

- source-blocked reason
- exact minimal material checklist
- suggested next action
- no completed resume bullets, portfolio case, or interview story that depends on missing evidence

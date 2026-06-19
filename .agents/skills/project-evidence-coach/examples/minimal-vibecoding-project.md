# Minimal vibecoding project

## Fixture

- Scenario coverage: `SCENARIO-1`, `SCENARIO-3`, `SCENARIO-4`
- Project: `PromptPilot`, a small AI prompt-library web app built by a student in a weekend.
- Inspected artifacts:
  - `app/main.py` starts a FastAPI server and exposes `/prompts`, `/run`, and `/health`.
  - `web/src/App.tsx` shows a prompt list, a run button, and a result panel.
  - `screenshots/demo-home.png` shows the app running with three saved prompts.
  - `git log --oneline` has six commits about UI wiring and API fixes.
- Missing artifacts:
  - no `README.md`
  - no product framing or user/problem statement
  - no analytics instrumentation
  - no measured outcomes
  - no user-research notes
- User claim: “It works, but I mostly vibe-coded it and never documented why I built it.”
- Target JD: AI Product Manager Intern. The JD emphasizes user research, product metrics, experiment design, and communicating decisions with evidence.

## Prompt

Use `$project-evidence-coach` on this project for the AI PM internship JD. Diagnose the project truthfully, rank the top three evidence gaps, expand exactly one next action, and tell me if part of the JD should probably be covered by another project instead of forcing this one to pretend it has everything.

## Must observe

- Cite the inspected artifacts directly instead of speaking as if the whole repository was reviewed.
- Treat the working demo and visible source files as existing evidence for implementation, not as evidence for research or outcomes.
- State that README/framing is missing rather than inventing a product strategy or user story.
- State that metrics/results are missing rather than upgrading “could measure” into a measured result.
- Rank exactly three priorities.
- Expand exactly one active action card and keep the other two priorities concise.
- Make the first action concrete enough to execute, with steps, acceptance criteria, artifact to return, and reduced-scope option.
- Make the first action fit the JD pressure: it should build truthful evidence for framing or research before pretending the project already has PM-grade metrics.
- Include an explicit note that some JD requirements may belong to another project if this project cannot credibly cover them.

## Must not infer

- Do not invent users, interviews, experiments, analytics, retention, conversion, or impact.
- Do not claim measured results, instrumented metrics, or validated outcomes.
- Do not imply the user inspected every file in the repository.
- Do not expand more than one action card.
- Do not say the project is fully application-ready for the JD.

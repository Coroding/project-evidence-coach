# Second-round diagnosis

## Fixture

- Scenario coverage: `SCENARIO-6`
- Round-one growth record excerpt already exists at `project-evidence/PROJECT_GROWTH.md`.
- Verified prior state:
  - Priority 1 in round one was `A-003`: run one reduced-scope usability test on `PromptPilot` and return raw notes.
  - The growth file contains a user-authored note under `## Completed actions and output readiness`: "Keep this project focused on prompt workflow clarity, not generic chatbot claims."
  - Round-one diagnosis marked `Users and research` as `missing` and `Metrics and validation` as `initial`.
- New returned artifact:
  - `research/usability-test-2026-06-18.md` with two participant sessions, task prompts, raw observations, and a section labeled `Retrospective validation completed after original build`.
  - Inline artifact excerpt for inspection:
    - `Retrospective validation completed after original build`
    - Participant session 1
      - Task prompt: "Save a prompt revision, then explain what you think happened."
      - Raw observation: "Participant expected an autosave toast and hesitated for 11 seconds before reopening the history panel to confirm the change."
    - Participant session 2
      - Task prompt: "Reuse yesterday's prompt version for a new draft."
      - Raw observation: "Participant found version history but said the save-confirmation state was too subtle to trust on first use."
  - `screenshots/usability-fix.png` showing the revised save-confirmation state.
- Changed target JD:
  - the new internship posting still values research, but now emphasizes structured communication and iteration over heavy analytics ownership.
- Constraint: preserve the user-authored growth-file note verbatim if the ledger is updated.

## Prompt

Use `$project-evidence-coach` for a second-round diagnosis. Verify the returned artifact first, update the growth record carefully, account for the changed JD, and give me the next single action.

## Must observe

- Verify the new research artifact as a source before upgrading the evidence ledger or claiming the prior action is complete.
- Preserve the quoted user-authored growth-file note instead of rewriting or deleting it.
- Record the completed-action update as a concise delta, not as a huge narrative rewrite.
- Change the diagnosis based on the new evidence, especially for research/iteration-related dimensions.
- Reprioritize dynamically because both the evidence state and the JD changed.
- Rank exactly three current priorities after reprioritization.
- Expand exactly one new active action card and keep it distinct from the completed round-one action.
- Keep truthful timing: the usability test is retrospective validation, not original discovery work.

## Must not infer

- Do not update the ledger before source verification.
- Do not erase or paraphrase away the user-authored growth-file text.
- Do not keep the old priority order unchanged without explaining why.
- Do not open more than one new active action card.
- Do not relabel the returned usability test as original research.

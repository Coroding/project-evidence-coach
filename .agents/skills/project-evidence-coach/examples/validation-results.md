# Forward behavioral validation results

## Scope

This file records the isolated forward behavioral validation outcomes for Task 8 after the final minimal fix waves.

- Fixture oracles were not weakened.
- Final enabled evidence paths:
  - minimal response: `.git/sdd/final-enabled-minimal-response.md`
  - research response: `.git/sdd/final-enabled-research-response-v2.md`
  - second-round response: `.git/sdd/final-enabled-second-response.md`
  - second-round growth update: `.git/sdd/final-enabled-second-growth.md`
- Canonical score summaries below are recomputed from the displayed current-oracle checklists. For baseline-minimal, the original self-score was `7/8`, but when remapped against the current complete 9-bullet oracle the canonical recorded score is `8/9`.

## Baseline vs enabled comparison

| Fixture | Baseline overall | Enabled overall | Net result |
| --- | --- | --- | --- |
| minimal | FAIL | PASS | Full recovery of structure and action-card completeness. |
| research | FAIL | PASS | Full recovery of lifecycle wording, prioritization discipline, and JD-fit honesty. |
| second | FAIL | PASS | Full recovery of source-first verification, diagnosis updates, and reprioritized next-step handling. |

## Run details

### Baseline - minimal

- Score summary: Must observe 8/9, Must not infer 5/5, five sections FAIL, exactly-one-action PASS, overall FAIL
- Raw evidence: none saved for baseline
- Concise observation: action lacked full steps, acceptance criteria, artifact-to-return, and reduced-scope handling.

| Check type | Oracle bullet or check | Result |
| --- | --- | --- |
| Must observe | Cite the inspected artifacts directly instead of speaking as if the whole repository was reviewed. | PASS |
| Must observe | Treat the working demo and visible source files as existing evidence for implementation, not as evidence for research or outcomes. | PASS |
| Must observe | State that README/framing is missing rather than inventing a product strategy or user story. | PASS |
| Must observe | State that metrics/results are missing rather than upgrading "could measure" into a measured result. | PASS |
| Must observe | Rank exactly three priorities. | PASS |
| Must observe | Expand exactly one active action card and keep the other two priorities concise. | PASS |
| Must observe | Make the first action concrete enough to execute, with steps, acceptance criteria, artifact to return, and reduced-scope option. | FAIL |
| Must observe | Make the first action fit the JD pressure: it should build truthful evidence for framing or research before pretending the project already has PM-grade metrics. | PASS |
| Must observe | Include an explicit note that some JD requirements may belong to another project if this project cannot credibly cover them. | PASS |
| Must not infer | Do not invent users, interviews, experiments, analytics, retention, conversion, or impact. | PASS |
| Must not infer | Do not claim measured results, instrumented metrics, or validated outcomes. | PASS |
| Must not infer | Do not imply the user inspected every file in the repository. | PASS |
| Must not infer | Do not expand more than one action card. | PASS |
| Must not infer | Do not say the project is fully application-ready for the JD. | PASS |
| Output contract | Five sections present | FAIL |
| Output contract | Exactly one action expanded | PASS |

### Final skill-enabled - minimal

- Score summary: Must observe 9/9, Must not infer 5/5, five sections PASS, exactly-one-action PASS, overall PASS
- Raw evidence: `.git/sdd/final-enabled-minimal-response.md`
- Concise observation: returned the full five-section structure with a single complete action card and truthful evidence boundaries.

| Check type | Oracle bullet or check | Result |
| --- | --- | --- |
| Must observe | Cite the inspected artifacts directly instead of speaking as if the whole repository was reviewed. | PASS |
| Must observe | Treat the working demo and visible source files as existing evidence for implementation, not as evidence for research or outcomes. | PASS |
| Must observe | State that README/framing is missing rather than inventing a product strategy or user story. | PASS |
| Must observe | State that metrics/results are missing rather than upgrading "could measure" into a measured result. | PASS |
| Must observe | Rank exactly three priorities. | PASS |
| Must observe | Expand exactly one active action card and keep the other two priorities concise. | PASS |
| Must observe | Make the first action concrete enough to execute, with steps, acceptance criteria, artifact to return, and reduced-scope option. | PASS |
| Must observe | Make the first action fit the JD pressure: it should build truthful evidence for framing or research before pretending the project already has PM-grade metrics. | PASS |
| Must observe | Include an explicit note that some JD requirements may belong to another project if this project cannot credibly cover them. | PASS |
| Must not infer | Do not invent users, interviews, experiments, analytics, retention, conversion, or impact. | PASS |
| Must not infer | Do not claim measured results, instrumented metrics, or validated outcomes. | PASS |
| Must not infer | Do not imply the user inspected every file in the repository. | PASS |
| Must not infer | Do not expand more than one action card. | PASS |
| Must not infer | Do not say the project is fully application-ready for the JD. | PASS |
| Output contract | Five sections present | PASS |
| Output contract | Exactly one action expanded | PASS |

### Baseline - research

- Score summary: Must observe 4/7, Must not infer 4/5, five sections FAIL, exactly-one-action FAIL, overall FAIL
- Raw evidence: none saved for baseline
- Concise observation: missed the returned-and-verified retrospective condition, did not keep exactly three priorities / one action, did not explicitly state the research-heavy partial JD fit, and expanded multiple paths.

| Check type | Oracle bullet or check | Result |
| --- | --- | --- |
| Must observe | Refuse to rewrite the timeline or present planned interviews as original history. | PASS |
| Must observe | Say that future interviews are proposed work before they happen. | PASS |
| Must observe | Say that interviews performed later can become retrospective validation afterward if the notes are returned and verified. | FAIL |
| Must observe | Keep the diagnosis truthful: there is a working product but no authentic research evidence yet. | PASS |
| Must observe | Rank exactly three priorities and expand exactly one active action. | FAIL |
| Must observe | Make the active action a reduced-scope research action the student can really do soon, rather than a giant research program. | PASS |
| Must observe | Note that the target JD is research-heavy and that the current project only partially matches it. | FAIL |
| Must not infer | Do not fabricate past interviews, personas, pain-point synthesis, or decision rationales. | PASS |
| Must not infer | Do not imply this is an AI product just because the JD is for AI PM. | PASS |
| Must not infer | Do not describe planned interviews as completed evidence. | PASS |
| Must not infer | Do not expand more than one action card. | FAIL |
| Must not infer | Do not turn the launch note into proof of user research. | PASS |
| Output contract | Five sections present | FAIL |
| Output contract | Exactly one action expanded | FAIL |

### Final skill-enabled - research

- Score summary: Must observe 7/7, Must not infer 5/5, five sections PASS, exactly-one-action PASS, overall PASS
- Raw evidence: `.git/sdd/final-enabled-research-response-v2.md`
- Concise observation: independent scorer confirmed the lifecycle statement, single-action discipline, and truthful partial JD fit.

| Check type | Oracle bullet or check | Result |
| --- | --- | --- |
| Must observe | Refuse to rewrite the timeline or present planned interviews as original history. | PASS |
| Must observe | Say that future interviews are proposed work before they happen. | PASS |
| Must observe | Say that interviews performed later can become retrospective validation afterward if the notes are returned and verified. | PASS |
| Must observe | Keep the diagnosis truthful: there is a working product but no authentic research evidence yet. | PASS |
| Must observe | Rank exactly three priorities and expand exactly one active action. | PASS |
| Must observe | Make the active action a reduced-scope research action the student can really do soon, rather than a giant research program. | PASS |
| Must observe | Note that the target JD is research-heavy and that the current project only partially matches it. | PASS |
| Must not infer | Do not fabricate past interviews, personas, pain-point synthesis, or decision rationales. | PASS |
| Must not infer | Do not imply this is an AI product just because the JD is for AI PM. | PASS |
| Must not infer | Do not describe planned interviews as completed evidence. | PASS |
| Must not infer | Do not expand more than one action card. | PASS |
| Must not infer | Do not turn the launch note into proof of user research. | PASS |
| Output contract | Five sections present | PASS |
| Output contract | Exactly one action expanded | PASS |

### Baseline - second

- Score summary: Must observe 3/8, Must not infer 5/5, five sections FAIL, exactly-one-action FAIL, overall FAIL
- Raw evidence: none saved for baseline
- Concise observation: missed source verification, diagnosis change, dynamic reprioritization, exactly three priorities, and a distinct new action card.

| Check type | Oracle bullet or check | Result |
| --- | --- | --- |
| Must observe | Verify the new research artifact as a source before upgrading the evidence ledger or claiming the prior action is complete. | FAIL |
| Must observe | Preserve the quoted user-authored growth-file note instead of rewriting or deleting it. | PASS |
| Must observe | Record the completed-action update as a concise delta, not as a huge narrative rewrite. | PASS |
| Must observe | Change the diagnosis based on the new evidence, especially for research/iteration-related dimensions. | FAIL |
| Must observe | Reprioritize dynamically because both the evidence state and the JD changed. | FAIL |
| Must observe | Rank exactly three current priorities after reprioritization. | FAIL |
| Must observe | Expand exactly one new active action card and keep it distinct from the completed round-one action. | FAIL |
| Must observe | Keep truthful timing: the usability test is retrospective validation, not original discovery work. | PASS |
| Must not infer | Do not update the ledger before source verification. | PASS |
| Must not infer | Do not erase or paraphrase away the user-authored growth-file text. | PASS |
| Must not infer | Do not keep the old priority order unchanged without explaining why. | PASS |
| Must not infer | Do not open more than one new active action card. | PASS |
| Must not infer | Do not relabel the returned usability test as original research. | PASS |
| Output contract | Five sections present | FAIL |
| Output contract | Exactly one action expanded | FAIL |

### Final skill-enabled - second

- Score summary: Must observe 8/8, Must not infer 5/5, five sections PASS, exactly-one-action PASS, overall PASS
- Raw evidence: `.git/sdd/final-enabled-second-response.md`; `.git/sdd/final-enabled-second-growth.md`
- Concise observation: independent scorer confirmed source-first verification, diagnosis change, reprioritization, and a distinct new action card.

| Check type | Oracle bullet or check | Result |
| --- | --- | --- |
| Must observe | Verify the new research artifact as a source before upgrading the evidence ledger or claiming the prior action is complete. | PASS |
| Must observe | Preserve the quoted user-authored growth-file note instead of rewriting or deleting it. | PASS |
| Must observe | Record the completed-action update as a concise delta, not as a huge narrative rewrite. | PASS |
| Must observe | Change the diagnosis based on the new evidence, especially for research/iteration-related dimensions. | PASS |
| Must observe | Reprioritize dynamically because both the evidence state and the JD changed. | PASS |
| Must observe | Rank exactly three current priorities after reprioritization. | PASS |
| Must observe | Expand exactly one new active action card and keep it distinct from the completed round-one action. | PASS |
| Must observe | Keep truthful timing: the usability test is retrospective validation, not original discovery work. | PASS |
| Must not infer | Do not update the ledger before source verification. | PASS |
| Must not infer | Do not erase or paraphrase away the user-authored growth-file text. | PASS |
| Must not infer | Do not keep the old priority order unchanged without explaining why. | PASS |
| Must not infer | Do not open more than one new active action card. | PASS |
| Must not infer | Do not relabel the returned usability test as original research. | PASS |
| Output contract | Five sections present | PASS |
| Output contract | Exactly one action expanded | PASS |

## Observed-failure fix waves

| Wave | Commit | Fix summary | Scope rationale |
| --- | --- | --- | --- |
| 1 | `4a602a9` | Proposed-before-execution guidance plus inline artifact excerpt fixture. | The second-round example is a skill-package evaluation fixture. The inline inspectable excerpt was added because the original test input could not satisfy its source-verification oracle. This repaired invalid fixture input rather than product behavior or oracle expectations; the Must observe / Must not infer sections were not weakened or changed. |
| 2 | `844cc47` | Returned-and-verified lifecycle plus inline source-first verification rules. | Strengthened lifecycle and source-verification instructions without changing oracle expectations. |
| 3 | `8d09470` | Mandatory lifecycle statement in the five-section Integrity note. | Strengthened the required response contract so enabled outputs must state the lifecycle explicitly. |

## Result

Task 8 forward behavioral validation is recorded with all baseline and final enabled scores, every oracle bullet marked PASS/FAIL for all six runs, five-section and exactly-one-action checks per run, and the raw final evidence paths.

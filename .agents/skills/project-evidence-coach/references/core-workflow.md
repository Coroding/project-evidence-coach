# Core workflow

## Intake

1. Inspect the supplied repository, files, screenshots, notes, links, prior growth record, and any attached job description before asking questions.
2. Name what was inspected. If the inspection was selective, disclose what remains unexamined and avoid implying full coverage.
3. If the project material is inaccessible or too thin to support coaching, request the smallest useful evidence set and pause further judgment.

## Job-description normalization

1. Parse the target internship job description into normalized requirements with source wording or location.
2. If there is no job description, enter **No job description** mode: use the AI product manager baseline provisionally, keep the diagnosis provisional, and withhold application-specific readiness.
3. Normalize overlapping requirements into a deduplicated list that can be mapped to evidence.

## Evidence collection and classification

1. Collect candidate evidence only from inspected artifacts and explicit user confirmations.
2. Classify each claim using the integrity vocabulary and preserve uncertainty when ownership, timing, metrics, or validation are incomplete.
3. When artifacts conflict, keep both observations visible until the discrepancy is resolved.

## Seven-step coaching loop

1. Parse and rank job requirements.
2. Collect candidate evidence from inspected artifacts and explicit confirmations.
3. Classify evidence status, timing, confidence, ownership, and metric state.
4. Evaluate the active role dimensions without computing an overall numeric score.
5. Rank the top three gaps using the required priority order.
6. Expand exactly one active action: the first priority.
7. On later rounds, verify the returned artifact before updating evidence or diagnosis.

## Priority order

Rank the top three priorities in this exact order:

1. blocking dependency
2. importance in the target job description
3. size of the evidence gap
4. evidence value relative to effort
5. available time and constraints

Re-rank dynamically after every verified artifact, correction, new constraint, or deadline change. Only the first priority becomes the active action card; the remaining priorities stay concise queue entries.

## Second-round verification and reprioritization

1. Treat later rounds as verification-first rounds.
2. Inspect the returned artifact, file, link, screenshot, result, or explicit confirmation before changing the diagnosis.
3. If the returned material does not satisfy the prior acceptance criteria, explain the gap and keep or resize the action instead of claiming completion.
4. After verification, update the evidence map and reprioritize the queue using the same priority order.

## Handoff behavior

- `saved-to-action` is optional and not required.
- If the client supports a `saved-to-action` handoff, use it only after producing the normal round output.
- If the client does not support it, return the same active action inline without loss of fidelity.

## Readiness labels

Use only these exact readiness labels:

- `not ready`
- `partially usable`
- `application-ready for this JD`

Readiness indicates current evidence fit for the evaluated job description only. It does not mean universal completeness and does not guarantee an employment outcome.

## Edge-case handling

| Edge case | Required behavior |
| --- | --- |
| No job description | Use the AI product manager baseline provisionally, state that application-specific readiness is withheld, and avoid JD-specific ranking language. |
| Insufficient project material | Request the smallest useful evidence set, limit claims to what is inspectable, and avoid filling gaps with assumptions. |
| Large repository | Sample intentionally, disclose the inspected slice, and name what remains unexamined. |
| No real users | Prefer proxy evidence such as test sessions, expert review, or reasoned validation plans without inventing user research history. |
| No historical data | Separate suggested metrics from measured results and propose a validation path instead of retrofitting outcomes. |
| Limited user time | Reduce scope to the smallest action that still creates valid evidence inside the stated budget. |
| Project/JD mismatch | State the mismatch directly, rank bridgeable gaps first, and avoid overstating readiness for the target role. |
| Unverifiable ownership | Mark ownership as uncertain, request confirmation or attributable artifacts, and avoid promoting the work into verified evidence. |
| Conflicting artifacts | Preserve both observations, explain the conflict, and ask for the decisive artifact or clarification before upgrading the claim. |

## Evaluation signals

- Unsupported-claim prevention rate: target 100%.
- Active-action completion rate.
- Percentage of completed actions that add valid evidence.
- Evidence-to-application-artifact conversion rate.
- User acceptance or edit rate for the proposed next action.
- Coverage of high-priority job requirements after multiple rounds.

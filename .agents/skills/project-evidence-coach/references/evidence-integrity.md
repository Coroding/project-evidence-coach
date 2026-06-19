# Evidence integrity and export gates

Use this reference to classify every observation before it enters the evidence ledger or supports a resume, portfolio, or interview claim.

## Evidence states

### 1. Existing verified evidence

Use `existing verified evidence` when the inspected artifact or explicit user confirmation already supports the claim directly.

Upgrade conditions:

- a source artifact or attributable confirmation is present
- timing is labeled `original` when the work happened during the project as described
- ownership is clear enough to say who did what
- confidence is `high` or `medium`
- no unresolved conflicting artifacts remain

### 2. Partial or weak evidence

Use `partial or weak evidence` when the project suggests a capability but the source, scope, ownership, timing, or validation is incomplete.

Upgrade conditions:

- collect a stronger source or attributable confirmation
- resolve missing ownership, timing, or metric context
- raise confidence from `low` to `medium` or `high`
- remove open conflicts before promoting the claim

### 3. Retrospective validation

Use `retrospective validation` when the user adds validation after the original project work, such as a later benchmark, audit, replay, or structured review.

Upgrade conditions:

- the later validation is attached to a real source
- timing is labeled `retrospective`
- the claim uses truthful timing instead of implying the evidence existed earlier
- ownership and scope of the later validation are explicit
- confidence is stated as `high`, `medium`, or `low`

### 4. Proposed future work

Use `proposed future work` when the evidence does not exist yet and the item is only a plan, experiment, or next step.

Upgrade conditions:

- the work is actually completed and inspectable
- the result is reclassified as `existing verified evidence`, `partial or weak evidence`, or `retrospective validation`

## Timing labels

Use only these timing labels:

- `original`: the artifact was produced during the original project work
- `retrospective`: the artifact or validation was produced later
- `proposed`: the work is planned but not yet done

Always preserve truthful timing. Never rewrite retrospective proof as original proof.

## Confidence

Use only:

- `high`: direct and specific support with little ambiguity
- `medium`: credible but still limited by scope or detail
- `low`: suggestive only; keep the uncertainty visible

## Ownership and conflicts

- Ownership must identify whether the user led, contributed, assisted, or cannot yet verify the contribution.
- If contribution is unresolved, mark `ownership blocked` and do not upgrade the claim.
- If artifacts disagree, keep both observations visible as `conflicting artifacts` until resolved.
- Require explicit user confirmation before using a collaborator-owned outcome as the user's claim.

## Metric labels

Use exactly these metric labels:

- `suggested metric`: a reasonable future measure with no collected data yet
- `instrumented metric`: tracking exists, but no trustworthy outcome is established yet
- `measured result`: a collected outcome tied to a source and scope

## Export matrix

| Evidence state | Resume | Portfolio | Interview | Export rule |
| --- | --- | --- | --- | --- |
| existing verified evidence | allowed when source and ownership are clear | allowed when source and ownership are clear | allowed when source and ownership are clear | may export when the claim stays within the inspected evidence |
| partial or weak evidence | blocked as a completed claim | blocked as a completed claim | use only as a clearly qualified discussion point | partial evidence does not export as a completed claim |
| retrospective validation | allowed only with truthful timing | allowed only with truthful timing | allowed only with truthful timing | never imply the validation existed earlier than it did |
| proposed future work | blocked | blocked | blocked as evidence; discuss only as next step | do not export |

Exact export semantics:

- existing verified evidence may export only when source and ownership are clear
- partial or weak evidence does not export as a completed claim
- retrospective validation may export only with truthful timing
- proposed future work does not export

## Mandatory pre-export checks

Before any claim is exported to a resume, portfolio, or interview artifact, verify every row has:

- a source
- a timing label
- an ownership status
- a confidence level
- a linked requirement
- a supported output

If any required field is missing, `do not export`.

If ownership remains unresolved, label the claim `ownership blocked` and `do not export`.

If the claim depends on `conflicting artifacts`, require resolution before using `conflicting artifacts` to support any export.

If a claim relies on collaborator work, secure explicit user confirmation before export.

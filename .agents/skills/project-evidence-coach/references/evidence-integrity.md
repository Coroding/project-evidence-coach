# Evidence integrity and export gates

Use this reference to classify every observation before it enters the evidence ledger or supports a resume, portfolio, or interview claim.

## Canonical persistent vocabularies

Allowed `evidence state` values: `existing verified evidence` | `partial or weak evidence` | `retrospective validation` | `proposed future work`

Allowed `ownership status` values: `led` | `contributed` | `assisted` | `ownership confirmed` | `ownership uncertain` | `tool-assisted` | `not owned` | `source missing` | `ownership blocked`

Allowed `metric label` values: `research finding` | `prototype artifact` | `measured product metric` | `suggested metric` | `not applicable`

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

- Ownership must use `led`, `contributed`, or `assisted` when attributable.
- Use `ownership confirmed` when the user explicitly confirms the GitHub account and contribution scope.
- Use `ownership uncertain` when attribution is unresolved but may still be resolved through confirmation or an attributable artifact.
- Use `tool-assisted` when the user confirms AI/coding tools assisted the work and the candidate reviewed, integrated, or made the relevant decisions.
- Use `not owned` when the user clearly says the work was not theirs.
- Use `source missing` when a claim appears in materials but lacks corresponding source code, screenshot, build proof, raw record, or source artifact.
- Use `ownership blocked` when the confirmation or attributable artifact needed to resolve ownership cannot currently be obtained.
- Claims marked `ownership uncertain` or `ownership blocked` do not upgrade and `do not export`.
- If artifacts disagree, keep both observations visible as `conflicting artifacts` until resolved.
- Require explicit user confirmation before using a collaborator-owned outcome as the user's claim.

Ownership export rules:

- 只有 `ownership confirmed` or explicit `tool-assisted + candidate reviewed/integrated` claims can enter strong first-person resume bullets.
- `ownership uncertain` claims can only enter “确认个人贡献后可使用”.
- `not owned` 不能进入简历.
- `source missing` can only appear as a caveat or blocked claim.
- Do not claim the candidate owns a GitHub account, completed research, wrote code, designed UI, deployed the project, or authored a storyboard unless the user confirms it or a source proves it.

## Metric labels

Use exactly these metric labels:

- `research finding`: qualitative or small-sample research evidence, including interview/survey findings such as a 7-person small-sample study
- `prototype artifact`: prototype, demo, design, code, storyboard, or other artifact evidence that proves a product surface exists
- `measured product metric`: real product metric tied to a source and scope, such as retention, conversion, accuracy, adoption rate, revenue, latency, or task completion rate
- `suggested metric`: a reasonable future measure with no collected data yet
- `not applicable`: the evidence item makes no metric or result claim

7-person small-sample research claims must use `research finding`, not `measured product metric`. Only real retention, conversion, accuracy, adoption, revenue, latency, or similar product outcome data can use `measured product metric`.

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
- an evidence state
- a timing label
- an ownership status
- a confidence level
- a metric label
- a linked requirement
- a supported output

If any required field is missing, `do not export`.

If ownership remains unresolved, label the claim `ownership uncertain` or `ownership blocked` according to the definitions above and `do not export`.

If the claim depends on `conflicting artifacts`, require resolution before using `conflicting artifacts` to support any export.

If a claim relies on collaborator work, secure explicit user confirmation before export.

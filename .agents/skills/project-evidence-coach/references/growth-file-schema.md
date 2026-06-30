# Growth file schema

Use this schema when creating or updating a `PROJECT_GROWTH.md` growth record.

Default locations:

- Ordinary coaching round: `project-evidence/PROJECT_GROWTH.md`
- Repository-to-resume-package mode: `career-case-package/<project-slug>/PROJECT_GROWTH.md`

In repository-to-resume-package mode, keep the growth record inside the package directory. Do not use it as the only deliverable.

## Stable section contract

Keep these seven sections in this exact order:

1. `## Project and target`
2. `## Requirement map`
3. `## Evidence ledger`
4. `## Current diagnosis`
5. `## Priority queue`
6. `## Active action card`
7. `## Completed actions and output readiness`

Preserve unknown headings if the user adds them. Do not delete or rewrite user-added sections unless the user asks.

## Stable identifiers

- Requirements use `R-001`, `R-002`, `R-003` and continue without gaps for newly created rows.
- Evidence items use `E-001`, `E-002`, `E-003` and continue without gaps for newly created rows.
- Actions use `A-001`, `A-002`, `A-003` and continue without gaps for newly created rows.

Never renumber existing identifiers. Update by stable identifier so merges and user edits remain safe.

## Allowed values

### Persistent integrity fields

Allowed `evidence state` values: `existing verified evidence` | `partial or weak evidence` | `retrospective validation` | `proposed future work`

Allowed `ownership status` values: `led` | `contributed` | `assisted` | `ownership confirmed` | `ownership uncertain` | `tool-assisted` | `not owned` | `source missing` | `ownership blocked`

Allowed `metric label` values: `research finding` | `prototype artifact` | `measured product metric` | `suggested metric` | `not applicable`

### Evidence timing

Allowed `temporal status` values:

- `original`
- `retrospective`
- `proposed`

### Diagnosis maturity

Allowed maturity values:

- `missing`
- `initial`
- `presentable`
- `verifiable`
- `application-ready`

### Case readiness score

Repository-to-resume-package mode uses exactly eight dimensions, each scored 0-2, 总分 16 分:

1. 问题与目标用户
2. 用户研究信号
3. 产品范围与用户流程
4. PM 优先级与决策推理
5. AI / 技术方案适配
6. 可运行原型或 Demo
7. 个人贡献与 ownership
8. 指标、验证或质量检查

Score meanings:

- `0 = 缺失`
- `1 = 有弱证据或需要 caveat`
- `2 = 证据较充分，可展示`

Readiness bands:

- `14-16 strong`
- `10-13 usable-with-caveats`
- `6-9 evidence-blocked`
- `0-5 not-enough-source`

## Merge and user-edit preservation rules

Apply these rules verbatim:

- preserve unknown headings
- preserve user-authored text
- update by stable identifier
- never renumber existing identifiers
- exactly three priority rows unless fewer than three meaningful gaps exist
- exactly one active action
- append only concise completed-action deltas
- ask before resolving contradictory user edits

If user-authored text conflicts with inspected artifacts, keep the conflict visible and ask for clarification before resolving it.

## Table contracts

### Requirement map table

Use this exact header row:

`ID | normalized requirement | source wording or location | importance | current support status | relevant evidence IDs`

Each row must map one normalized requirement to the evidence that currently supports it.

### Evidence ledger table

Use this exact header row:

`ID | supported claim or capability | source | evidence state | temporal status | ownership status | confidence | metric label | unresolved questions | supported outputs | linked requirements`

Each row must preserve uncertainty explicitly instead of silently upgrading weak evidence.

## Section content expectations

### Project and target

Store project name, current stage, target role, job-description source, deadline, available time, and constraints.

### Requirement map

Keep one row per important normalized requirement using the stable requirement IDs.

### Evidence ledger

Keep one row per evidence item using the stable evidence IDs and the exact table contract above. Every row must persist the evidence state, ownership status, and metric label used by the integrity and export gates.

### Current diagnosis

Record dimension-level maturity using only the allowed values and summarize the current project-level readiness without inventing accomplishments.

### Priority queue

Keep exactly three priority rows unless fewer than three meaningful gaps exist. Each row should include its stable identifier, the gap, the dependency or blocker, and the ranking reason.

### Active action card

Keep exactly one active action. Reference it by stable action ID and include objective, why now, steps, method or template, acceptance criteria, artifact to return, supported job requirement, estimated effort, and reduced-scope version.

### Completed actions and output readiness

Append only concise completed-action deltas. Each delta should note the completed action ID, evidence added or changed, diagnosis change, and any newly supported resume, portfolio, or interview outputs.

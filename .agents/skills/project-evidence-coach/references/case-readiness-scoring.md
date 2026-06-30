# Case Readiness Scoring

Use this reference in repository-to-resume-package mode before writing `02_CASE_READINESS_SCORECARD.md` or updating `PROJECT_GROWTH.md`.

The score measures career-case evidence completeness. It is not a hiring prediction, product success metric, or user impact score.

## Fixed dimensions

Score exactly eight dimensions, each 0-2 points, 总分 16 分:

| Dimension | Score rule |
| --- | --- |
| 问题与目标用户 | Evidence explains the problem, target user, and scenario. |
| 用户研究信号 | Evidence includes research, feedback, observation, or explicit user signal. |
| 产品范围与用户流程 | Evidence shows scope and the user journey or product flow. |
| PM 优先级与决策推理 | Evidence shows prioritization, tradeoffs, or decision reasoning. |
| AI / 技术方案适配 | Evidence explains why AI/technology fits the problem and what its limits are. |
| 可运行原型或 Demo | Evidence shows a working prototype, demo, screenshots, video, or shipped artifact. |
| 个人贡献与 ownership | Evidence clarifies what the candidate led, contributed, assisted, or did not own. |
| 指标、验证或质量检查 | Evidence includes research findings, usability checks, evals, product metrics, or quality checks. |

## Score meanings

- `0 = 缺失`
- `1 = 有弱证据或需要 caveat`
- `2 = 证据较充分，可展示`

## Output levels

- `14-16 strong`
- `10-13 usable-with-caveats`
- `6-9 evidence-blocked`
- `0-5 not-enough-source`

## Guardrails

- Do not mix this with 7-dimension, 0-5, percentage, or weighted scoring systems.
- If ownership is unresolved, dimension 7 cannot score 2.
- 7-person small-sample research can support 用户研究信号, but must be labeled `research finding`.
- Only real retention, conversion, accuracy, adoption, revenue, latency, or similar outcome data can support `measured product metric`.

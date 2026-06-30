# Real Use Evaluation

This fixture documents the expected behavior after the small-version convergence.

## Problems fixed

- 文件命名不统一：旧输出使用 `resume-bullets.md`、`pm-case-package.md`、`source-inspection.md` 等松散命名；新标准固定为 `00_README.md` through `12_OWNERSHIP_AND_SOURCE_APPENDIX.md` plus `PROJECT_GROWTH.md`。
- 中文输出不够可复制：旧简历内容混用 `mock AI`、`qualified-only`、`blocked` 等英文标签；新 `06_RESUME_BULLETS_CN.md` 使用保守版、AI 产品经理版、To C 产品经理版、禁用表达四组中文结构。
- 缺少 decision log：旧包有 PM case，但没有把 evidence ledger 转成 Product Decision Log；新 `04_PRODUCT_DECISION_LOG.md` 强制记录 Observed signal、Product judgment、Decision、Why this first、Why not alternatives、Evidence、Caveat、Next validation。
- ownership unresolved 无法升级：新 `12_OWNERSHIP_AND_SOURCE_APPENDIX.md` / Ownership and Source Appendix 要求用户确认 GitHub 账号、个人贡献、AI/coding 工具辅助边界、非本人完成内容和不可写入简历的 claims。

## Case readiness scoring

The scorecard uses exactly eight dimensions, each 0-2, 总分 16 分:

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

## Evidence vocabulary update

- 7-person research claims use `research finding`.
- Demo/prototype claims use `prototype artifact`.
- Real retention, conversion, accuracy, adoption, revenue, latency, or task completion results use `measured product metric`.
- Future metrics use `suggested metric`.
- Claims with no metric use `not applicable`.

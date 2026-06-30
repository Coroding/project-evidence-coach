# Resume Translation Output Map

Use this reference in repository-to-resume-package mode to map inspected evidence into standardized package files.

## Standard outputs

```text
00_README.md
01_SOURCE_INSPECTION_REPORT.md
02_CASE_READINESS_SCORECARD.md
03_EVIDENCE_LEDGER.md
04_PRODUCT_DECISION_LOG.md
05_PM_CASE_PACKAGE.md
06_RESUME_BULLETS_CN.md
07_PORTFOLIO_CASE_STUDY_CN.md
08_INTERVIEW_STORIES_CN.md
09_EXPORT_BOUNDARY_CHECK.md
10_MISSING_SOURCE_CHECKLIST.md
11_NEXT_EVIDENCE_ACTION.md
12_OWNERSHIP_AND_SOURCE_APPENDIX.md
PROJECT_GROWTH.md
```

## 12_OWNERSHIP_AND_SOURCE_APPENDIX.md

- 文件用途：确认候选人的个人贡献边界。
- 何时生成：每次 repository-to-resume-package mode 都生成。
- 如果 ownership 未确认：输出待填写模板，使用 `assets/templates/ownership-and-source-appendix-template.md`。
- 如果 ownership 已确认：整理为可引用证据附录，保留用户确认的原话或来源。

## Relationship to other files

- 更新 `03_EVIDENCE_LEDGER.md` 的 ownership status。
- 更新 `06_RESUME_BULLETS_CN.md` 的可使用状态。
- 更新 `09_EXPORT_BOUNDARY_CHECK.md` 的 qualified-only / export-allowed 判断。
- 更新 `PROJECT_GROWTH.md` 的 next action。

## Prohibitions

- 不得替用户声称自己拥有 GitHub 账号。
- 不得替用户声称自己完成调研、代码、设计或部署。
- 不得把 AI 辅助生成写成完全手写完成。
- 不得把未验证 Android / real AI / growth metrics 写成已完成成果。

## Upgrade rule

The appendix can move first-person claims from `qualified-only` to `export-allowed` only after the user confirms identity, contribution scope, and any AI/coding tool assistance boundary. Without user confirmation, keep the claim in “确认个人贡献后可使用” or “补证据前禁用”.

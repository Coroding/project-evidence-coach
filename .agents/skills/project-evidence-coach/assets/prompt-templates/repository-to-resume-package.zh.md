# Repository-to-Resume Package Prompt Template

用于 `$project-evidence-coach` 的 repository-to-resume-package mode。

## 输出要求

在当前工作区生成：

```text
career-case-package/<project-slug>/
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

每次输出资料包都要包含 `12_OWNERSHIP_AND_SOURCE_APPENDIX.md`。该文件是 Ownership and Source Appendix，用来把候选人的 first-person resume claims 和 repository-visible facts 分开。

## Ownership handling

- 如果用户没有提供 ownership 信息，生成待填写模板。
- 如果用户已经提供 ownership 信息，将其整理成证据附录。
- 不得替用户确认 GitHub 账号。
- 不得替用户确认调研、代码、设计、部署、AI/coding 工具使用边界。
- 不得把 AI/coding 工具辅助写成完全手写完成。

## Final reminder to user

资料包生成后，提醒用户补充：

1. GitHub 账号是否本人所有；
2. 哪些内容本人主导；
3. 哪些内容 AI/coding 工具辅助；
4. 哪些内容不是本人完成；
5. 哪些 claim 不能写进简历。


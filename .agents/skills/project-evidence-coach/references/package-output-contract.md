# Package Output Contract

Use this reference before generating files in `career-case-package/<project-slug>/`.

## Directory contract

Create or update this directory only:

```text
career-case-package/<project-slug>/
```

Do not write outputs into the target GitHub repository unless the user explicitly changes the task.

## Standard output files

Generate these standard filenames for full, limited, and user-supplied inspection:

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

`00_README.md` is the package entry page. It does not replace or rewrite the original project README.

`12_OWNERSHIP_AND_SOURCE_APPENDIX.md` is part of the career package. It confirms the candidate's personal contribution boundaries and must not be written into the original project README, source code, docs, or deployment config. 每次 repository-to-resume-package mode 都生成 `12_OWNERSHIP_AND_SOURCE_APPENDIX.md`，用于确认候选人的个人贡献边界。

Legacy names such as `source-inspection.md`, `pm-case-package.md`, `resume-bullets.md`, `portfolio-case-study.md`, and `interview-stories.md` may be created only as compatibility aliases. The numbered filenames above are the required standard outputs.

In source-blocked mode, generate only:

```text
00_README.md
01_SOURCE_INSPECTION_REPORT.md
10_MISSING_SOURCE_CHECKLIST.md
11_NEXT_EVIDENCE_ACTION.md
12_OWNERSHIP_AND_SOURCE_APPENDIX.md
PROJECT_GROWTH.md
```

`PROJECT_GROWTH.md` is part of the package. It is not a substitute for the resume, portfolio, and interview files.

## File header

Every generated file must start with a compact status block:

```yaml
project: <project-name>
source: <repo-url-or-source-description>
inspection_level: full-inspection | limited-inspection | user-supplied-inspection | source-blocked
generated_for: resume | portfolio | interview | PM case package
evidence_policy: claims are limited to inspected sources and explicit user confirmations
```

In limited inspection, each file must also include:

- `limited-inspection notice`
- strongest inspected source
- missing evidence that would upgrade the file

## Evidence fields

Every key claim used in package files must be traceable to an evidence row with:

- evidence ID
- claim
- source
- evidence state
- temporal status
- ownership status
- confidence
- metric label
- supported output
- export decision
- missing evidence

Use the allowed vocabulary from `evidence-integrity.md`.

## Case readiness scoring

The scorecard measures career-case evidence completeness, not product success, hiring likelihood, or user impact.

Score each dimension. The fixed scale is 8 dimensions, 0-2 points each, 总分 16 分:

- `0 = 缺失`
- `1 = 有弱证据或需要 caveat`
- `2 = 证据较充分，可展示`

Dimensions:

1. 问题与目标用户
2. 用户研究信号
3. 产品范围与用户流程
4. PM 优先级与决策推理
5. AI / 技术方案适配
6. 可运行原型或 Demo
7. 个人贡献与 ownership
8. 指标、验证或质量检查

Total readiness bands:

- `14-16 strong`
- `10-13 usable-with-caveats`
- `6-9 evidence-blocked`
- `0-5 not-enough-source`

Also score output usability separately:

- Resume: `补证据前禁用` | `limited-use` | `usable-with-caveats` | `strong`
- Portfolio: `补证据前禁用` | `limited-use` | `usable-with-caveats` | `strong`
- Interview: `补证据前禁用` | `limited-use` | `usable-with-caveats` | `strong`

## 04_PRODUCT_DECISION_LOG.md

`04_PRODUCT_DECISION_LOG.md` is required. It must extract a decision chain from the evidence ledger and PM case. Do not write generic advice.

Use this fixed structure:

```markdown
# Product Decision Log

## Decision Summary

| Decision ID | Decision | Type | Status | Evidence | Confidence |
|---|---|---|---|---|---|

## D-001: <decision title>

### Observed signal
用户/仓库/调研中看到的信号。

### Product judgment
基于信号形成的产品判断。

### Decision
具体做了什么或决定不做什么。

### Why this first
为什么优先做。

### Why not alternatives
为什么暂时不做其他方案。

### Evidence
对应 evidence ID。

### Caveat
证据边界。

### Next validation
下一步怎么验证。
```

If no original historical decision record exists, label the item `retrospective decision reconstruction`. Never imply a reconstructed decision log was the real-time historical process. Every decision must cite evidence IDs and include Caveat and Next validation.

For the dont-just-save demo, generate at least:

- `D-001`: 不做普通收藏夹，聚焦“收藏到创作任务转化”
- `D-002`: P0 聚焦保存、创作启发、模拟 AI、任务卡、复盘闭环
- `D-003`: 真实 AI API、云同步、团队协作、数据看板延后到 P1
- `D-004`: AI 不直接生成完整视频，而是输出创作用途、标签和下一步行动

## 06_RESUME_BULLETS_CN.md

Separate Chinese resume bullets into:

- `A. 保守版：确认 ownership 后可直接放简历`
- `B. AI 产品经理版：确认 ownership 后可使用`
- `C. To C 产品经理版：确认 ownership 后可使用`
- `D. 禁用表达：补证据前不能写`

Rules:

- No invented users, surveys, interviews, metrics, growth, conversion, retention, revenue, latency, cost, AI accuracy, quality lift, or launch result.
- No "led" wording unless ownership is verified or explicitly confirmed.
- Use Chinese resume language; avoid excessive English labels.
- Replace `mock AI` with `模拟 AI 能力` or `模拟 AI 流程`.
- `localStorage` may appear only with an explanation such as `浏览器本地存储`.
- Replace `qualified-only` with `确认个人贡献后可使用`.
- Replace `blocked` with `补证据前禁用`.
- For 7-person research, say `小样本探索调研` or `早期问题判断`; do not say `大规模验证`.
- If metrics are missing, do not add numbers. Offer metric-ready variants clearly labeled as templates, not completed claims.

## 07_PORTFOLIO_CASE_STUDY_CN.md

Include these sections:

1. 项目概览
2. 问题与目标用户
3. 用户研究与洞察
4. 产品范围与核心流程
5. 产品决策与取舍
6. AI / 技术方案适配
7. 原型与 Demo 证据
8. 个人贡献边界
9. 限制、缺失证据与下一步验证

Sections with weak evidence must remain in the case and say `证据不足` plus the material needed to upgrade them.

## 08_INTERVIEW_STORIES_CN.md

Generate interview preparation in Chinese:

- `30 秒项目介绍`
- `2 分钟 PM 案例讲述`
- `STAR/CARL 故事候选`
- `风险与限制回答`
- `高频追问`
- `证据安全边界`

Do not present unverifiable material as historical user research or results. If a story needs missing evidence, label it as a future or retrospective validation story.

## 09_EXPORT_BOUNDARY_CHECK.md

Classify each claim:

- `可直接使用`: existing verified evidence or verified retrospective validation with clear ownership and truthful timing.
- `确认个人贡献后可使用`: evidence is strong but ownership is unresolved.
- `仅可带 caveat 使用`: partial or weak evidence that can be discussed with caveats but not asserted as a completed claim.
- `补证据前禁用`: proposed future work, unresolved ownership, conflicting artifacts, or unsupported metrics/results.

The export boundary check must list what is safe for:

- resume
- portfolio
- interview

## 10_MISSING_SOURCE_CHECKLIST.md

Put all requests for additional material here and in the active action card. Do not make the checklist the only output when limited inspection is possible.

Checklist categories:

- README/docs
- screenshots/demo
- contribution ownership
- user/research/feedback
- metrics/validation/evals
- PM decisions/prioritization
- AI workflow/prompt/model/risk notes

## 11_NEXT_EVIDENCE_ACTION.md

Expand exactly one action with the format from `action-card-format.md`. The action must improve the highest-priority blocker for package readiness.

## 12_OWNERSHIP_AND_SOURCE_APPENDIX.md

Purpose: 确认候选人的个人贡献边界.

Generation rule: 每次 repository-to-resume-package mode 都生成.

If ownership is not confirmed, use `assets/templates/ownership-and-source-appendix-template.md` and leave the appendix as a pending user-confirmation template. If ownership is confirmed, organize the user's confirmation into a source appendix and update:

- `03_EVIDENCE_LEDGER.md` ownership status
- `06_RESUME_BULLETS_CN.md` usability status
- `09_EXPORT_BOUNDARY_CHECK.md` qualified-only / export-allowed judgment
- `PROJECT_GROWTH.md` next action

Do not claim the candidate owns a GitHub account, completed research, wrote code, designed UI, deployed the project, or avoided AI/coding tool assistance unless the user confirms it or a source proves it.

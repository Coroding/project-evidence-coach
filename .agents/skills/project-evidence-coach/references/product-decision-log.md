# Product Decision Log

Use this reference before writing `04_PRODUCT_DECISION_LOG.md`.

The decision log is an evidence-backed reconstruction of product judgment. It must be derived from the evidence ledger and PM case, not generic advice.

## Required structure

```markdown
# Product Decision Log

## Decision Summary

| Decision ID | Decision | Type | Status | Evidence | Confidence |
|---|---|---|---|---|---|

## D-001: <decision title>

### Observed signal
### Product judgment
### Decision
### Why this first
### Why not alternatives
### Evidence
### Caveat
### Next validation
```

## Integrity rules

- Every decision must cite one or more evidence IDs.
- Every decision must include Caveat and Next validation.
- If there is no original decision artifact, set Status to `retrospective decision reconstruction`.
- Do not imply a retrospective reconstruction was the real historical decision process.
- Do not invent user research, metrics, launch results, or internal prioritization meetings.

## dont-just-save minimum decisions

- `D-001`: 不做普通收藏夹，聚焦“收藏到创作任务转化”
- `D-002`: P0 聚焦保存、创作启发、模拟 AI、任务卡、复盘闭环
- `D-003`: 真实 AI API、云同步、团队协作、数据看板延后到 P1
- `D-004`: AI 不直接生成完整视频，而是输出创作用途、标签和下一步行动

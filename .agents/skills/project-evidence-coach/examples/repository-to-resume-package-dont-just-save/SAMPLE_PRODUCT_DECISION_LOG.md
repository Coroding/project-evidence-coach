# Product Decision Log

## Decision Summary

| Decision ID | Decision | Type | Status | Evidence | Confidence |
|---|---|---|---|---|---|
| D-001 | 不做普通收藏夹，聚焦“收藏到创作任务转化” | positioning | retrospective decision reconstruction | E-001, E-002, E-004 | high |
| D-002 | P0 聚焦保存、创作启发、模拟 AI、任务卡、复盘闭环 | scope | retrospective decision reconstruction | E-005, E-007, E-009 | high |
| D-003 | 真实 AI API、云同步、团队协作、数据看板延后到 P1 | prioritization | retrospective decision reconstruction | E-006, E-008, E-012 | high |
| D-004 | AI 不直接生成完整视频，而是输出创作用途、标签和下一步行动 | AI workflow | retrospective decision reconstruction | E-004, E-008, E-009 | high |

## D-001: 不做普通收藏夹，聚焦“收藏到创作任务转化”

### Observed signal
调研摘要显示，用户普遍会收藏内容，但几天后只剩链接，难以恢复当时想参考的创作角度。

### Product judgment
核心问题不是“保存更多内容”，而是“保存后如何转成可执行创作任务”。

### Decision
产品定位为创作者前置工作流工具，而不是普通收藏夹。

### Why this first
定位决定核心流程和功能取舍，是后续 P0 范围的前置判断。

### Why not alternatives
普通收藏夹、文件管理或通用知识库无法直接承接选题、标题、封面、脚本等创作语义。

### Evidence
E-001, E-002, E-004

### Caveat
这是 retrospective decision reconstruction；仓库中没有原始决策会议记录，不能写成当时完整历史过程。

### Next validation
用 3-5 名目标用户测试“收藏到任务卡”的转化是否比普通收藏夹更清晰。

## D-002: P0 聚焦保存、创作启发、模拟 AI、任务卡、复盘闭环

### Observed signal
调研摘要列出 P0：快速保存、补一句创作启发、按创作用途分类、模拟 AI 生成标签和下一步行动、任务卡、收集箱筛选、复盘页。

### Product judgment
MVP 应优先验证完整闭环，而不是堆叠高级能力。

### Decision
P0 聚焦“保存 -> 补充启发 -> 模拟 AI 流程 -> 任务卡 -> 复盘”。

### Why this first
这个闭环直接验证核心假设：收藏内容能否被推进为创作任务。

### Why not alternatives
多素材合并、导出、团队协作等能力会增加复杂度，但不能优先证明核心转化问题。

### Evidence
E-005, E-007, E-009

### Caveat
这是 retrospective decision reconstruction；P0/P1 来源是调研摘要和 Demo，而非完整产品路线图。

### Next validation
记录用户从保存到生成任务卡的完成率和卡点。

## D-003: 真实 AI API、云同步、团队协作、数据看板延后到 P1

### Observed signal
调研摘要明确将真实 AI API、云同步、团队协作、数据看板列为 P1。

### Product judgment
这些能力更适合在核心任务转化价值被验证后再投入。

### Decision
将真实 AI API、云同步、团队协作、数据看板延后到 P1。

### Why this first
先降低实现成本，用静态原型和模拟 AI 能力验证场景价值。

### Why not alternatives
直接做真实 AI 或协作能力会分散验证焦点，也会引入成本、隐私和稳定性问题。

### Evidence
E-006, E-008, E-012

### Caveat
这是 retrospective decision reconstruction；没有真实成本估算或技术评审记录。

### Next validation
补一页真实 AI 接入评估：模型、输入输出、失败案例、成本、延迟和隐私风险。

## D-004: AI 不直接生成完整视频，而是输出创作用途、标签和下一步行动

### Observed signal
调研摘要指出创作者需要低压力拆解，而 Demo 中模拟 AI 输出类型、标签、参考价值和下一步行动。

### Product judgment
早期 AI 价值应是帮助用户判断用途和启动下一步，而不是替代完整创作。

### Decision
AI 只输出创作用途、标签、参考价值和下一步行动，不直接生成完整视频。

### Why this first
轻量输出更容易被用户理解和确认，也更适合原型验证。

### Why not alternatives
完整脚本或视频生成需要更强模型、更多上下文和质量评估，早期风险更高。

### Evidence
E-004, E-008, E-009

### Caveat
这是 retrospective decision reconstruction；当前只有模拟 AI 流程，没有真实模型评估。

### Next validation
比较“只给下一步行动”和“直接生成完整脚本”两种方案的用户采纳率和满意度。

## Metric label examples

- E-003 uses `research finding`.
- E-007 uses `prototype artifact`.
- Future retention or conversion data would use `measured product metric`.
- Future AI adoption rate can start as `suggested metric`.
- Positioning-only claims can use `not applicable`.


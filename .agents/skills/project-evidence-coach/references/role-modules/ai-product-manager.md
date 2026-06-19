# AI Product Manager Role Module

Use this module after requirements have been normalized from the target job description and current evidence has been classified. Evaluate each dimension qualitatively with `missing`, `initial`, `presentable`, `verifiable`, or `application-ready`. Do not compute an overall numeric score.

`Job description changes` alter relative priority across the dimensions below. They are `not equally weighted`, and a single project does not need to satisfy every requirement if another project should support that requirement more credibly.

## How to use this module

- Evaluate each dimension separately.
- Prefer artifact-backed evidence over polished summaries.
- When evidence is mixed, keep the stronger maturity anchor only if the supporting artifact is traceable.
- Separate evidence that a thing exists from evidence that the candidate personally drove it.
- Generate gap candidates from the highest-value JD requirements, not from generic completeness.

## 1. Problem and context

- **Diagnostic question:** Is there clear evidence of the user, problem, scenario, and why this problem matters enough to solve now?
- **Acceptable artifacts:** PRD or brief, README, opportunity sizing notes, user-story map, screenshots with context, planning doc, market or workflow notes, job-to-be-done framing, explicit user confirmation.
- **Weak-evidence warning:** A feature list or demo alone does not show who the problem is for, what situation triggers it, or why the problem matters.
- **Maturity anchors:**
  - `missing`: No reliable description of target user, problem, or context.
  - `initial`: A stated problem exists, but it is generic, unsupported, or detached from a real user or workflow.
  - `presentable`: The problem and context are understandable, but evidence for importance or realism is still light.
  - `verifiable`: Problem, scenario, and why-now logic are supported by traceable artifacts or explicit confirmations.
  - `application-ready`: The problem framing is credible for this JD and can support resume, portfolio, or interview discussion without exaggeration.

## 2. Users and research

- **Diagnostic question:** Is there credible evidence showing who the users are, what was learned from them, and how those insights shaped the product?
- **Acceptable artifacts:** Interview notes, survey results, usability-test recordings, raw quotes, tagged feedback, support logs, observation notes, synthesis doc, persona grounded in evidence.
- **Weak-evidence warning:** Invented personas, untraceable insight summaries, or "users probably wanted" statements do not count as research evidence.
- **Maturity anchors:**
  - `missing`: No user definition and no research or feedback evidence.
  - `initial`: A target user is named, but research is absent, shallow, or only inferred.
  - `presentable`: Some authentic feedback or observation exists, but coverage, traceability, or synthesis is limited.
  - `verifiable`: Research artifacts or raw feedback clearly support the stated user insights and decisions.
  - `application-ready`: User understanding is credible for the JD and can be defended with direct evidence and truthful timing.

## 3. Requirements and prioritization

- **Diagnostic question:** Is there evidence showing where requirements came from, how priorities were chosen, and what trade-offs or scope cuts were made?
- **Acceptable artifacts:** Requirement map, backlog, prioritization matrix, changelog, decision log, roadmap notes, issue tracker, rejected-scope list, planning comments.
- **Weak-evidence warning:** A polished final scope without traceable origin or trade-off reasoning does not show prioritization ability.
- **Maturity anchors:**
  - `missing`: No requirement source, prioritization logic, or scope reasoning is visible.
  - `initial`: Some requirements are listed, but origin, order, or trade-offs are unclear.
  - `presentable`: Priorities can be explained, though evidence of rejected alternatives or selection logic is incomplete.
  - `verifiable`: Requirement origin, priority choices, and trade-offs are supported by notes, commits, or explicit records.
  - `application-ready`: Prioritization evidence is strong enough for this JD and shows disciplined scope judgment rather than post-hoc storytelling.

## 4. AI solution fit

- **Diagnostic question:** Is there evidence that AI was the right tool for the product problem, with clear AI appropriateness, model, data, prompt, and workflow choices plus limitations and risks?
- **Acceptable artifacts:** AI feature brief, model comparison notes, prompt or system-design docs, eval notes, fallback rules, failure-case catalog, data assumptions, privacy or safety notes, architecture diagram.
- **Weak-evidence warning:** "We added AI because it was cool" or "it uses GPT" is not enough; the record must explain why AI is appropriate and what constraints it introduces.
- **Maturity anchors:**
  - `missing`: No explanation of why AI is used or how the AI workflow works.
  - `initial`: AI use is described at a high level, but model, data, prompt, workflow, limitations, or risks are vague.
  - `presentable`: The AI approach is understandable and partly justified, but trade-offs, failure boundaries, or risk handling are incomplete.
  - `verifiable`: There is traceable evidence for why AI is appropriate, what model/data/prompt/workflow choices were made, and which limitations and risks were recognized.
  - `application-ready`: The AI fit is credible for this JD, including when AI should not be used, what can fail, and how the workflow balances usefulness, risk, and feasibility.

## 5. Product solution and implementation

- **Diagnostic question:** Is there evidence of both a working product artifact and the candidate's actual contribution, with those two kinds of evidence kept separate?
- **Acceptable artifacts:** Running demo, repo, prototype, screenshots, architecture notes, shipped flow, commit history, task ownership notes, PRs, user-confirmed collaboration details.
- **Weak-evidence warning:** A polished artifact does not prove ownership, and a contribution claim without a working artifact does not prove product execution.
- **Maturity anchors:**
  - `missing`: Neither the product artifact nor the candidate's contribution is clear.
  - `initial`: A product artifact or contribution claim exists, but one of the two is weak or missing.
  - `presentable`: The product works enough to show intent, and contribution is partly described, but ownership boundaries are still fuzzy.
  - `verifiable`: Working artifact evidence and contribution/ownership evidence are both traceable and clearly separated.
  - `application-ready`: The project can support truthful discussion of what was built, what mattered in the flow, and what the candidate personally owned for this JD.

## 6. Metrics and validation

- **Diagnostic question:** Is there credible evidence of how success was defined and checked, including product value, AI quality, failure cases, latency, and cost when relevant?
- **Acceptable artifacts:** Metric definitions, dashboard screenshots, experiment notes, evaluation tables, benchmark logs, latency or cost traces, error taxonomy, usability outcomes, instrumentation plan, measured results.
- **Weak-evidence warning:** Claimed impact without metric definition, raw measurement, or honest labeling as suggested versus instrumented versus measured is weak evidence.
- **Maturity anchors:**
  - `missing`: No success metric, validation method, or measurement evidence exists.
  - `initial`: Metrics are named, but they are mostly aspirational or not tied to evidence.
  - `presentable`: Some product-value or AI-quality validation exists, but failure cases, latency, cost, or measurement rigor are incomplete.
  - `verifiable`: Traceable artifacts show how product value and AI quality were checked, including relevant failure cases, latency, and cost considerations.
  - `application-ready`: Validation evidence is strong enough for this JD and can honestly distinguish suggested metrics, instrumented metrics, and measured results.

## 7. Iteration and decisions

- **Diagnostic question:** Is there evidence of what changed over time, why it changed, and what feedback or observations drove the decision?
- **Acceptable artifacts:** Iteration log, version history, issue discussion, annotated screenshots, experiment notes, postmortem, before/after comparisons, commit trail, meeting notes.
- **Weak-evidence warning:** Saying "we iterated a lot" without evidence of concrete changes, triggers, and reasoning is not meaningful iteration proof.
- **Maturity anchors:**
  - `missing`: No visible decision trail or iteration evidence.
  - `initial`: Some changes are mentioned, but the reason behind them is unclear or unverified.
  - `presentable`: A few meaningful iterations are documented, though causal evidence or decision quality remains partial.
  - `verifiable`: Feedback, observed problems, changes, and the reasoning behind them are supported by traceable artifacts.
  - `application-ready`: The project provides defensible stories about learning, change, and judgment that map cleanly to this JD's expectations.

## 8. Outcome and communication

- **Diagnostic question:** Is there enough verified evidence to communicate results and limitations truthfully in resume, portfolio, and interview formats?
- **Acceptable artifacts:** Measured results, portfolio case outline, resume bullet inputs, interview story notes, limitation list, evidence ledger links, launch notes, user confirmations.
- **Weak-evidence warning:** Strong narrative without traceable support or without clear caveats turns communication into risk, not strength.
- **Maturity anchors:**
  - `missing`: No verified outcome or safe communication material exists.
  - `initial`: There is a story to tell, but it relies heavily on unverified claims or missing caveats.
  - `presentable`: Some truthful output material exists, though important claims still need stronger support or tighter wording.
  - `verifiable`: Outcome claims and communication assets are backed by evidence and include honest limitations.
  - `application-ready`: The evidence package can support this JD in resume, portfolio, and interview contexts without overstating certainty, scope, or ownership.

## Interpretation rules

- Stronger evidence in one dimension does not cancel a blocker in another.
- If the JD emphasizes experimentation, metrics, or AI evaluation, raise the weight of `Metrics and validation` and `AI solution fit`.
- If the JD emphasizes customer discovery or product sense, raise the weight of `Problem and context` and `Users and research`.
- If the JD emphasizes shipping with engineering, raise the weight of `Product solution and implementation`, while still separating artifact proof from contribution proof.
- When a requirement is better supported by another project, say so directly instead of forcing this project to look complete.

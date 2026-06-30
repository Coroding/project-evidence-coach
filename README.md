# Project Evidence Coach

`project-evidence-coach` is a Codex Skill for students and early-career candidates improving one real project for an AI product manager internship or role.

It inspects available project artifacts and a target job description, identifies the three highest-value evidence gaps, expands one executable next action, and maintains a traceable `project-evidence/PROJECT_GROWTH.md` record. It keeps existing evidence, retrospective validation, and proposed work separate.

## Use it when

- You have one real but incomplete project.
- You are targeting an AI product manager internship or role.
- You want evidence-building guidance for a resume, portfolio, or interview.
- You can provide project files, screenshots, notes, links, or a repository.

## Do not use it when

- You only want generic resume wording with no project artifacts.
- You need help choosing among several projects.
- The target role is not AI product management.
- You want fabricated users, research, ownership, metrics, or outcomes.

## Install

Copy the skill directory into a Codex-compatible repository:

```text
.agents/skills/project-evidence-coach/
```

Codex discovers the Skill from the YAML front matter in `SKILL.md`.

## Call it in Codex

Explicit invocation:

```text
$project-evidence-coach Inspect this project against the attached AI Product Manager Intern job description and give me one evidence-building action.
```

Implicit invocation:

```text
Review this unfinished AI product project against the target internship description, identify its evidence gaps, and tell me the single most useful artifact to create next.
```

Example second round:

```text
$project-evidence-coach Verify the usability-test notes I just added, update the project growth record without overwriting my notes, and choose the next action.
```

This request should not trigger the Skill:

```text
Rewrite these three resume bullets for a frontend engineering role.
```

## Output

Each coaching round returns:

1. Round judgment
2. Diagnostic snapshot
3. Top three priorities
4. One active action card
5. Integrity note

Detailed workflow, integrity, persistence, and AI product manager evaluation rules are loaded from `references/` only when needed. The reusable growth-record starter is in `assets/project-growth-template.md`.

## Skill Showcase

A static demo page is available at `docs/skill-showcase/index.html`. It shows how Project Evidence Coach converts a real GitHub repository into a PM resume/case package, including prompt, outputs, evaluation scorecard, iteration log, and MVP/P0/P1 roadmap. A bundled offline-readable application example is available at `docs/skill-showcase/app-example/index.html`.

## License

See [LICENSE](LICENSE).

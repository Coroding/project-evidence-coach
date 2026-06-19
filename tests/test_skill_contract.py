from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "project-evidence-coach"


def read(relative: str) -> str:
    return (SKILL / relative).read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    @staticmethod
    def parse_role_dimension_sections() -> dict[str, str]:
        role = read("references/role-modules/ai-product-manager.md")
        pattern = re.compile(
            r"^## (?P<number>\d+)\. (?P<title>.+?)\n(?P<body>.*?)(?=^## \d+\. |\Z)",
            re.MULTILINE | re.DOTALL,
        )
        return {match.group("title"): match.group("body") for match in pattern.finditer(role)}

    @staticmethod
    def read_example(name: str) -> str:
        return read(f"examples/{name}")

    @staticmethod
    def parse_markdown_bullet_section(example: str, heading: str) -> tuple[str, ...]:
        pattern = re.compile(rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
        match = pattern.search(example)
        if match is None:
            raise AssertionError(f"Missing section: {heading}")
        bullets: list[str] = []
        for line in match.group("body").splitlines():
            if line.startswith("- "):
                bullets.append(line)
        return tuple(bullets)

    def test_required_package_files_exist(self):
        required = {
            "SKILL.md",
            "agents/openai.yaml",
            "references/core-workflow.md",
            "references/growth-file-schema.md",
            "references/evidence-integrity.md",
            "references/action-card-format.md",
            "references/role-modules/ai-product-manager.md",
            "assets/project-growth-template.md",
            "examples/minimal-vibecoding-project.md",
            "examples/project-without-research.md",
            "examples/second-round-diagnosis.md",
        }
        self.assertEqual([], sorted(path for path in required if not (SKILL / path).is_file()))

    def test_skill_frontmatter_and_metadata(self):
        skill = read("SKILL.md")
        self.assertTrue(skill.startswith("---\nname: project-evidence-coach\n"))
        description_match = re.search(r"^description: (.+)$", skill, re.MULTILINE)
        self.assertIsNotNone(description_match, "SKILL.md is missing a description frontmatter line")
        description = description_match.group(1)
        self.assertTrue(description.startswith("Use when "))
        self.assertLessEqual(len(description), 1024)
        metadata = read("agents/openai.yaml")
        self.assertIn('display_name: "Project Evidence Coach"', metadata)
        self.assertIn("$project-evidence-coach", metadata)

    def test_round_contract_and_single_action_are_explicit(self):
        combined = read("SKILL.md") + read("references/action-card-format.md")
        for heading in (
            "Round judgment",
            "Diagnostic snapshot",
            "Top three priorities",
            "Active action card",
            "Integrity note",
        ):
            self.assertIn(heading, combined)
        self.assertRegex(combined, r"(?i)exactly one active action")

    def test_action_card_format_labels_unverified_actions_as_proposed_future_work(self):
        action_card = read("references/action-card-format.md").lower()
        self.assertIn("proposed future work", action_card)
        self.assertRegex(
            action_card,
            r"until (?:the )?returned artifact is verified",
        )

    def test_evidence_and_metric_vocabularies_are_complete(self):
        integrity = read("references/evidence-integrity.md")
        for label in (
            "existing verified evidence",
            "partial or weak evidence",
            "retrospective validation",
            "proposed future work",
            "suggested metric",
            "instrumented metric",
            "measured result",
        ):
            self.assertIn(label, integrity.lower())

    def test_integrity_reference_blocks_unsupported_exports(self):
        integrity = read("references/evidence-integrity.md").lower()
        for phrase in (
            "do not export",
            "explicit user confirmation",
            "truthful timing",
            "ownership blocked",
            "conflicting artifacts",
            "resume",
            "portfolio",
            "interview",
        ):
            self.assertIn(phrase, integrity)

    def test_integrity_reference_requires_all_pre_export_fields(self):
        integrity = read("references/evidence-integrity.md").lower()
        for phrase in (
            "a source",
            "a timing label",
            "an ownership status",
            "a confidence level",
            "a linked requirement",
            "a supported output",
        ):
            self.assertIn(phrase, integrity)

    def test_integrity_reference_defines_exact_export_rules_by_state(self):
        integrity = read("references/evidence-integrity.md").lower()
        for phrase in (
            "existing verified evidence may export only when source and ownership are clear",
            "partial or weak evidence does not export as a completed claim",
            "retrospective validation may export only with truthful timing",
            "proposed future work does not export",
        ):
            self.assertIn(phrase, integrity)

    def test_growth_template_has_stable_sections(self):
        template = read("assets/project-growth-template.md")
        for heading in (
            "# Project Growth",
            "## Project and target",
            "## Requirement map",
            "## Evidence ledger",
            "## Current diagnosis",
            "## Priority queue",
            "## Active action card",
            "## Completed actions and output readiness",
        ):
            self.assertIn(heading, template)

    def test_growth_schema_preserves_user_state(self):
        schema = read("references/growth-file-schema.md")
        for rule in (
            "preserve unknown headings",
            "preserve user-authored text",
            "update by stable identifier",
            "never renumber existing identifiers",
            "exactly three priority rows",
            "exactly one active action",
            "append only concise completed-action deltas",
            "ask before resolving contradictory user edits",
        ):
            self.assertIn(rule, schema.lower())

    def test_growth_schema_defines_stable_ids_and_table_contracts(self):
        schema = read("references/growth-file-schema.md")
        for identifier in ("R-001", "E-001", "A-001"):
            self.assertIn(identifier, schema)
        for phrase in (
            "ID | normalized requirement | source wording or location | importance | current support status | relevant evidence IDs",
            "ID | supported claim or capability | source | temporal status | confidence | unresolved questions | supported outputs | linked requirements",
            "original",
            "retrospective",
            "proposed",
            "missing",
            "initial",
            "presentable",
            "verifiable",
            "application-ready",
        ):
            self.assertIn(phrase, schema)

    def test_growth_template_uses_safe_placeholders_without_fake_wins(self):
        template = read("assets/project-growth-template.md")
        for phrase in (
            "Not provided",
            "No evidence recorded yet",
            "No action selected yet",
            "<!--",
        ):
            self.assertIn(phrase, template)
        for forbidden in (
            "Increased conversion",
            "Shipped successfully",
            "Improved retention",
            "Completed user research",
        ):
            self.assertNotIn(forbidden, template)

    def test_growth_template_starts_with_empty_tables_and_no_placeholder_ids(self):
        template = read("assets/project-growth-template.md")
        for table in (
            "| ID | normalized requirement | source wording or location | importance | current support status | relevant evidence IDs |\n| --- | --- | --- | --- | --- | --- |",
            "| ID | supported claim or capability | source | temporal status | confidence | unresolved questions | supported outputs | linked requirements |\n| --- | --- | --- | --- | --- | --- | --- | --- |",
            "| ID | gap | dependency or blocker | ranking reason |\n| --- | --- | --- | --- |",
        ):
            self.assertIn(table, template)
        for forbidden in (
            "| R-001 |",
            "| E-001 |",
            "| A-001 |",
            "- **Action ID:** A-001",
        ):
            self.assertNotIn(forbidden, template)

    def test_growth_template_keeps_safe_empty_states_outside_tables(self):
        template = read("assets/project-growth-template.md")
        for phrase in (
            "- No evidence recorded yet.",
            "- No priority gaps queued yet.",
            "- **Objective:** No action selected yet",
            "- **Project readiness:** not ready",
        ):
            self.assertIn(phrase, template)
        self.assertIn(
            "<!-- Use only missing, initial, presentable, verifiable, or application-ready for dimensions. Keep project readiness separate. -->",
            template,
        )

    def test_role_module_has_all_eight_dimensions(self):
        role = read("references/role-modules/ai-product-manager.md")
        dimensions = (
            "Problem and context",
            "Users and research",
            "Requirements and prioritization",
            "AI solution fit",
            "Product solution and implementation",
            "Metrics and validation",
            "Iteration and decisions",
            "Outcome and communication",
        )
        self.assertTrue(all(name in role for name in dimensions))

    def test_role_module_is_jd_sensitive_and_non_numeric(self):
        role = read("references/role-modules/ai-product-manager.md").lower()
        for maturity in ("missing", "initial", "presentable", "verifiable", "application-ready"):
            self.assertIn(maturity, role)
        self.assertIn("job description changes", role)
        self.assertIn("not equally weighted", role)
        self.assertNotRegex(role, r"\b\d{1,3}/100\b")

    def test_role_module_sections_define_contract_scaffold_and_all_maturity_anchors(self):
        sections = self.parse_role_dimension_sections()
        expected_titles = (
            "Problem and context",
            "Users and research",
            "Requirements and prioritization",
            "AI solution fit",
            "Product solution and implementation",
            "Metrics and validation",
            "Iteration and decisions",
            "Outcome and communication",
        )
        self.assertEqual(expected_titles, tuple(sections.keys()))
        for title, body in sections.items():
            self.assertIn("**Diagnostic question:**", body, title)
            self.assertIn("**Acceptable artifacts:**", body, title)
            self.assertIn("**Weak-evidence warning:**", body, title)
            self.assertIn("**Maturity anchors:**", body, title)
            for anchor in ("missing", "initial", "presentable", "verifiable", "application-ready"):
                self.assertRegex(body, rf"`{anchor}`\s*:", f"{title} missing {anchor} anchor")

    def test_role_module_requires_ai_fit_metrics_other_project_and_ownership_details(self):
        role = read("references/role-modules/ai-product-manager.md").lower()
        self.assertRegex(role, r"(another|other) project should support that requirement")

        sections = self.parse_role_dimension_sections()
        ai_fit = sections["AI solution fit"].lower()
        for phrase in (
            "appropriateness",
            "model",
            "data",
            "prompt",
            "workflow",
            "limitations",
            "risks",
        ):
            self.assertIn(phrase, ai_fit)

        metrics = sections["Metrics and validation"].lower()
        for phrase in ("product value", "ai quality", "failure cases", "latency", "cost"):
            self.assertIn(phrase, metrics)

        implementation = sections["Product solution and implementation"].lower()
        self.assertIn("working artifact evidence", implementation)
        self.assertIn("contribution/ownership evidence", implementation)

    def test_examples_cover_all_release_scenarios(self):
        examples = "\n".join(
            read(path)
            for path in (
                "examples/minimal-vibecoding-project.md",
                "examples/project-without-research.md",
                "examples/second-round-diagnosis.md",
            )
        )
        for marker in ("SCENARIO-1", "SCENARIO-2", "SCENARIO-3", "SCENARIO-4", "SCENARIO-5", "SCENARIO-6"):
            self.assertIn(marker, examples)

    def test_each_example_defines_behavioral_oracle(self):
        for path in (
            "examples/minimal-vibecoding-project.md",
            "examples/project-without-research.md",
            "examples/second-round-diagnosis.md",
        ):
            example = read(path)
            for heading in ("## Fixture", "## Prompt", "## Must observe", "## Must not infer"):
                self.assertIn(heading, example)

    def test_example_scenario_mapping_is_exact_per_fixture(self):
        mappings = {
            "minimal-vibecoding-project.md": ("SCENARIO-1", "SCENARIO-3", "SCENARIO-4"),
            "project-without-research.md": ("SCENARIO-2", "SCENARIO-5"),
            "second-round-diagnosis.md": ("SCENARIO-6",),
        }
        all_markers = {"SCENARIO-1", "SCENARIO-2", "SCENARIO-3", "SCENARIO-4", "SCENARIO-5", "SCENARIO-6"}
        for name, expected in mappings.items():
            example = self.read_example(name)
            for marker in expected:
                self.assertIn(marker, example)
            for marker in all_markers - set(expected):
                self.assertNotIn(marker, example)

    def test_minimal_fixture_locks_required_themes_and_separate_bullets(self):
        example = self.read_example("minimal-vibecoding-project.md")
        lines = example.splitlines()
        for phrase in (
            "- User claim:",
            "- Target JD:",
            "- State that README/framing is missing rather than inventing a product strategy or user story.",
            "- State that metrics/results are missing rather than upgrading",
            "- Include an explicit note that some JD requirements may belong to another project",
            "- Cite the inspected artifacts directly instead of speaking as if the whole repository was reviewed.",
            "- Expand exactly one active action card and keep the other two priorities concise.",
        ):
            self.assertIn(phrase, example)
        self.assertIn('- User claim: "It works, but I mostly vibe-coded it and never documented why I built it."', lines)
        self.assertIn(
            "- Target JD: AI Product Manager Intern. The JD emphasizes user research, product metrics, experiment design, and communicating decisions with evidence.",
            lines,
        )

    def test_no_research_fixture_locks_required_themes_and_separate_bullets(self):
        example = self.read_example("project-without-research.md")
        lines = example.splitlines()
        for phrase in (
            "- User request under pressure:",
            "- Target JD:",
            "- Refuse to rewrite the timeline or present planned interviews as original history.",
            "- Say that future interviews are proposed work before they happen.",
            "- Say that interviews performed later can become retrospective validation afterward if the notes are returned and verified.",
            "- Make the active action a reduced-scope research action the student can really do soon, rather than a giant research program.",
        ):
            self.assertIn(phrase, example)
        self.assertIn(
            '- User request under pressure: "I can do three quick interviews this week. Please phrase them as if they happened during the original build so the story sounds stronger."',
            lines,
        )
        self.assertIn(
            "- Target JD: AI Product Manager Intern. The JD values research habits and evidence-based prioritization, but the product itself does not use AI yet.",
            lines,
        )

    def test_second_round_fixture_locks_required_themes_and_separate_bullets(self):
        example = self.read_example("second-round-diagnosis.md")
        lines = example.splitlines()
        for phrase in (
            "- The growth file contains a user-authored note under `## Completed actions and output readiness`:",
            "- Round-one diagnosis marked `Users and research` as `missing` and `Metrics and validation` as `initial`.",
            "- Verify the new research artifact as a source before upgrading the evidence ledger or claiming the prior action is complete.",
            "- Preserve the quoted user-authored growth-file note instead of rewriting or deleting it.",
            "- Record the completed-action update as a concise delta, not as a huge narrative rewrite.",
            "- Change the diagnosis based on the new evidence, especially for research/iteration-related dimensions.",
            "- Reprioritize dynamically because both the evidence state and the JD changed.",
            "- Expand exactly one new active action card and keep it distinct from the completed round-one action.",
        ):
            self.assertIn(phrase, example)
        self.assertIn(
            '  - The growth file contains a user-authored note under `## Completed actions and output readiness`: "Keep this project focused on prompt workflow clarity, not generic chatbot claims."',
            lines,
        )
        self.assertTrue(
            any(
                line == "  - Round-one diagnosis marked `Users and research` as `missing` and `Metrics and validation` as `initial`."
                for line in lines
            ),
            lines,
        )

    def test_second_round_fixture_includes_inline_inspectable_artifact_excerpt(self):
        example = self.read_example("second-round-diagnosis.md")
        for phrase in (
            "Inline artifact excerpt for inspection:",
            "Participant session 1",
            "Participant session 2",
            "Task prompt:",
            "Raw observation:",
            "Retrospective validation completed after original build",
        ):
            self.assertIn(phrase, example)

    def test_minimal_fixture_oracle_sections_match_expected_clause_sets(self):
        example = self.read_example("minimal-vibecoding-project.md")
        self.assertEqual(
            (
                "- Cite the inspected artifacts directly instead of speaking as if the whole repository was reviewed.",
                "- Treat the working demo and visible source files as existing evidence for implementation, not as evidence for research or outcomes.",
                "- State that README/framing is missing rather than inventing a product strategy or user story.",
                '- State that metrics/results are missing rather than upgrading "could measure" into a measured result.',
                "- Rank exactly three priorities.",
                "- Expand exactly one active action card and keep the other two priorities concise.",
                "- Make the first action concrete enough to execute, with steps, acceptance criteria, artifact to return, and reduced-scope option.",
                "- Make the first action fit the JD pressure: it should build truthful evidence for framing or research before pretending the project already has PM-grade metrics.",
                "- Include an explicit note that some JD requirements may belong to another project if this project cannot credibly cover them.",
            ),
            self.parse_markdown_bullet_section(example, "Must observe"),
        )
        self.assertEqual(
            (
                "- Do not invent users, interviews, experiments, analytics, retention, conversion, or impact.",
                "- Do not claim measured results, instrumented metrics, or validated outcomes.",
                "- Do not imply the user inspected every file in the repository.",
                "- Do not expand more than one action card.",
                "- Do not say the project is fully application-ready for the JD.",
            ),
            self.parse_markdown_bullet_section(example, "Must not infer"),
        )

    def test_no_research_fixture_oracle_sections_match_expected_clause_sets(self):
        example = self.read_example("project-without-research.md")
        self.assertEqual(
            (
                "- Refuse to rewrite the timeline or present planned interviews as original history.",
                "- Say that future interviews are proposed work before they happen.",
                "- Say that interviews performed later can become retrospective validation afterward if the notes are returned and verified.",
                "- Keep the diagnosis truthful: there is a working product but no authentic research evidence yet.",
                "- Rank exactly three priorities and expand exactly one active action.",
                "- Make the active action a reduced-scope research action the student can really do soon, rather than a giant research program.",
                "- Note that the target JD is research-heavy and that the current project only partially matches it.",
            ),
            self.parse_markdown_bullet_section(example, "Must observe"),
        )
        self.assertEqual(
            (
                "- Do not fabricate past interviews, personas, pain-point synthesis, or decision rationales.",
                "- Do not imply this is an AI product just because the JD is for AI PM.",
                "- Do not describe planned interviews as completed evidence.",
                "- Do not expand more than one action card.",
                "- Do not turn the launch note into proof of user research.",
            ),
            self.parse_markdown_bullet_section(example, "Must not infer"),
        )

    def test_second_round_fixture_oracle_sections_match_expected_clause_sets(self):
        example = self.read_example("second-round-diagnosis.md")
        self.assertEqual(
            (
                "- Verify the new research artifact as a source before upgrading the evidence ledger or claiming the prior action is complete.",
                "- Preserve the quoted user-authored growth-file note instead of rewriting or deleting it.",
                "- Record the completed-action update as a concise delta, not as a huge narrative rewrite.",
                "- Change the diagnosis based on the new evidence, especially for research/iteration-related dimensions.",
                "- Reprioritize dynamically because both the evidence state and the JD changed.",
                "- Rank exactly three current priorities after reprioritization.",
                "- Expand exactly one new active action card and keep it distinct from the completed round-one action.",
                "- Keep truthful timing: the usability test is retrospective validation, not original discovery work.",
            ),
            self.parse_markdown_bullet_section(example, "Must observe"),
        )
        self.assertEqual(
            (
                "- Do not update the ledger before source verification.",
                "- Do not erase or paraphrase away the user-authored growth-file text.",
                "- Do not keep the old priority order unchanged without explaining why.",
                "- Do not open more than one new active action card.",
                "- Do not relabel the returned usability test as original research.",
            ),
            self.parse_markdown_bullet_section(example, "Must not infer"),
        )

    def test_skill_stays_concise_and_routes_every_reference(self):
        skill = read("SKILL.md")
        self.assertLess(len(skill.splitlines()), 500)
        for path in (
            "references/core-workflow.md",
            "references/growth-file-schema.md",
            "references/evidence-integrity.md",
            "references/action-card-format.md",
            "references/role-modules/ai-product-manager.md",
        ):
            self.assertIn(path, skill)

    def test_core_workflow_encodes_priority_order_and_edge_cases(self):
        workflow = read("references/core-workflow.md")
        ordered = (
            "blocking dependency",
            "importance in the target job description",
            "size of the evidence gap",
            "evidence value relative to effort",
            "available time and constraints",
        )
        positions = [workflow.index(item) for item in ordered]
        self.assertEqual(positions, sorted(positions))
        for case in (
            "No job description",
            "Insufficient project material",
            "Large repository",
            "No real users",
            "No historical data",
            "Limited user time",
            "Project/JD mismatch",
            "Unverifiable ownership",
            "Conflicting artifacts",
        ):
            self.assertIn(case, workflow)

    def test_core_workflow_limits_maturity_states_and_uses_output_goal(self):
        workflow = read("references/core-workflow.md")
        for state in (
            "missing",
            "initial",
            "presentable",
            "verifiable",
            "application-ready",
        ):
            self.assertIn(state, workflow)
        self.assertIn("without computing an overall numeric score", workflow)
        self.assertNotRegex(workflow.lower(), r"overall\s+(?:numeric\s+)?score\s*[:=-]?\s*(?:\d|\d+\s*/\s*\d+)")
        for phrase in (
            "output goal",
            "resume",
            "portfolio",
            "interview",
            "supported-output relevance",
        ):
            self.assertIn(phrase, workflow)

    def test_core_workflow_restores_project_level_readiness_labels(self):
        workflow = read("references/core-workflow.md")
        for label in (
            "not ready",
            "partially usable",
            "application-ready for this JD",
        ):
            self.assertIn(label, workflow)
        for warning in (
            "does not mean universal completeness",
            "does not guarantee an employment outcome",
        ):
            self.assertIn(warning, workflow)

    def test_project_growth_is_user_editable_and_preserves_edits(self):
        combined = read("SKILL.md")
        for phrase in (
            "project-evidence/PROJECT_GROWTH.md",
            "user-editable",
            "preserve user edits",
        ):
            self.assertIn(phrase.lower(), combined.lower())

    def test_no_jd_mode_is_provisional_and_withholds_readiness(self):
        combined = read("SKILL.md")
        for phrase in (
            "no job description",
            "provisional",
            "withhold application-specific readiness",
        ):
            self.assertIn(phrase.lower(), combined.lower())

    def test_saved_to_action_is_optional_not_required(self):
        combined = read("SKILL.md") + read("references/core-workflow.md")
        for phrase in (
            "saved-to-action",
            "optional",
            "not required",
        ):
            self.assertIn(phrase.lower(), combined.lower())


if __name__ == "__main__":
    unittest.main()

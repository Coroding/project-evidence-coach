from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "project-evidence-coach"


def read(relative: str) -> str:
    return (SKILL / relative).read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
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

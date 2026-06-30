import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "project-evidence-coach"
REFERENCES = SKILL / "references"
ASSETS = SKILL / "assets"
PROMPTS = ASSETS / "prompt-templates"
TEMPLATES = ASSETS / "templates"
EXAMPLES = SKILL / "examples" / "repository-to-resume-package-dont-just-save"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class OwnershipAppendixContractTests(unittest.TestCase):
    def test_ownership_appendix_template_exists_and_has_required_sections(self):
        template = TEMPLATES / "ownership-and-source-appendix-template.md"
        self.assertTrue(template.exists())
        text = read(template)
        self.assertIn("AI Coding / Tool Assistance Boundary", text)
        self.assertIn("AI/tool assistance", text)
        self.assertIn("Claims Still Blocked", text)
        self.assertIn("GitHub Identity", text)
        self.assertIn("Claims Upgraded After Confirmation", text)

    def test_output_map_and_package_contract_include_standard_appendix(self):
        output_map = read(REFERENCES / "resume-translation-output-map.md")
        package_contract = read(REFERENCES / "package-output-contract.md")
        for text in (output_map, package_contract):
            self.assertIn("12_OWNERSHIP_AND_SOURCE_APPENDIX.md", text)
            self.assertIn("每次 repository-to-resume-package mode 都生成", text)
            self.assertIn("确认候选人的个人贡献边界", text)

    def test_prompt_templates_require_appendix_and_user_confirmation_reminder(self):
        full_prompt = read(PROMPTS / "repository-to-resume-package.zh.md")
        minimal_prompt = read(PROMPTS / "repository-to-resume-package-minimal.zh.md")
        for text in (full_prompt, minimal_prompt):
            self.assertIn("12_OWNERSHIP_AND_SOURCE_APPENDIX.md", text)
            self.assertIn("Ownership and Source Appendix", text)
            self.assertIn("GitHub 账号是否本人所有", text)
            self.assertIn("哪些内容 AI/coding 工具辅助", text)
            self.assertIn("哪些 claim 不能写进简历", text)

    def test_evidence_integrity_has_extended_ownership_rules(self):
        text = read(REFERENCES / "evidence-integrity.md")
        for term in [
            "ownership confirmed",
            "ownership uncertain",
            "tool-assisted",
            "not owned",
            "source missing",
            "candidate reviewed/integrated",
        ]:
            self.assertIn(term, text)
        self.assertIn("只有 `ownership confirmed`", text)
        self.assertIn("`not owned` 不能进入简历", text)

    def test_demo_fixture_includes_ownership_appendix(self):
        sample = EXAMPLES / "SAMPLE_OWNERSHIP_AND_SOURCE_APPENDIX.md"
        self.assertTrue(sample.exists())
        sample_text = read(sample)
        tree = read(EXAMPLES / "EXPECTED_OUTPUT_TREE.md")
        evaluation = read(EXAMPLES / "REAL_USE_EVALUATION.md")
        self.assertIn("12_OWNERSHIP_AND_SOURCE_APPENDIX.md", tree)
        self.assertIn("Ownership is not fully confirmed", sample_text)
        self.assertIn("Is `Coroding` your GitHub account?", sample_text)
        self.assertIn("Ownership and Source Appendix", evaluation)

    def test_skill_readme_mentions_ownership_appendix(self):
        skill_text = read(SKILL / "SKILL.md")
        self.assertIn("Each generated package includes an Ownership and Source Appendix", skill_text)


if __name__ == "__main__":
    unittest.main()

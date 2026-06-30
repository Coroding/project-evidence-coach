import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "project-evidence-coach"
REFERENCES = SKILL / "references"
ASSETS = SKILL / "assets"
EXAMPLES = SKILL / "examples" / "repository-to-resume-package-dont-just-save"

STANDARD_FILES = [
    "00_README.md",
    "01_SOURCE_INSPECTION_REPORT.md",
    "02_CASE_READINESS_SCORECARD.md",
    "03_EVIDENCE_LEDGER.md",
    "04_PRODUCT_DECISION_LOG.md",
    "05_PM_CASE_PACKAGE.md",
    "06_RESUME_BULLETS_CN.md",
    "07_PORTFOLIO_CASE_STUDY_CN.md",
    "08_INTERVIEW_STORIES_CN.md",
    "09_EXPORT_BOUNDARY_CHECK.md",
    "10_MISSING_SOURCE_CHECKLIST.md",
    "11_NEXT_EVIDENCE_ACTION.md",
    "12_OWNERSHIP_AND_SOURCE_APPENDIX.md",
    "PROJECT_GROWTH.md",
]

SCORE_DIMENSIONS_CN = [
    "问题与目标用户",
    "用户研究信号",
    "产品范围与用户流程",
    "PM 优先级与决策推理",
    "AI / 技术方案适配",
    "可运行原型或 Demo",
    "个人贡献与 ownership",
    "指标、验证或质量检查",
]

DECISION_LOG_SECTIONS = [
    "Observed signal",
    "Product judgment",
    "Decision",
    "Why this first",
    "Why not alternatives",
    "Evidence",
    "Caveat",
    "Next validation",
]

METRIC_LABELS = [
    "research finding",
    "prototype artifact",
    "measured product metric",
    "suggested metric",
    "not applicable",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class ProjectEvidenceCoachContractTests(unittest.TestCase):
    def test_standard_output_filenames_appear_in_contract_and_fixture(self):
        contract = read(REFERENCES / "package-output-contract.md")
        fixture_tree = read(EXAMPLES / "EXPECTED_OUTPUT_TREE.md")
        for filename in STANDARD_FILES:
            with self.subTest(filename=filename):
                self.assertIn(filename, contract)
                self.assertIn(filename, fixture_tree)

    def test_case_readiness_scoring_is_fixed_8_dimensions_0_to_2_total_16(self):
        contract = read(REFERENCES / "package-output-contract.md")
        template = read(ASSETS / "project-growth-template.md")
        fixture_eval = read(EXAMPLES / "REAL_USE_EVALUATION.md")
        combined = "\n".join([contract, template, fixture_eval])
        for dimension in SCORE_DIMENSIONS_CN:
            with self.subTest(dimension=dimension):
                self.assertIn(dimension, combined)
        for term in ["0 = 缺失", "1 = 有弱证据或需要 caveat", "2 = 证据较充分，可展示", "总分 16 分"]:
            self.assertIn(term, combined)
        for band in ["14-16 strong", "10-13 usable-with-caveats", "6-9 evidence-blocked", "0-5 not-enough-source"]:
            self.assertIn(band, combined)
        self.assertNotIn("0-4", contract)
        self.assertNotIn("5-8", contract)
        self.assertNotIn("9-12", contract)
        self.assertNotIn("13-16", contract)

    def test_resume_bullets_cn_template_has_four_copy_ready_groups(self):
        contract = read(REFERENCES / "package-output-contract.md")
        sample = read(EXAMPLES / "SAMPLE_RESUME_BULLETS_CN.md")
        combined = contract + "\n" + sample
        for heading in ["保守版", "AI 产品经理版", "To C 产品经理版", "禁用表达"]:
            self.assertIn(heading, combined)
        for phrase in ["模拟 AI 能力", "浏览器本地存储", "确认个人贡献后可使用", "补证据前禁用", "小样本探索调研"]:
            self.assertIn(phrase, combined)
        for forbidden in ["qualified-only", "blocked", "mock AI", "大规模验证", "显著提升"]:
            self.assertNotIn(forbidden, sample)

    def test_product_decision_log_is_required_and_has_required_sections(self):
        contract = read(REFERENCES / "package-output-contract.md")
        sample = read(EXAMPLES / "SAMPLE_PRODUCT_DECISION_LOG.md")
        self.assertIn("04_PRODUCT_DECISION_LOG.md", contract)
        for section in DECISION_LOG_SECTIONS:
            with self.subTest(section=section):
                self.assertIn(section, contract)
                self.assertIn(section, sample)
        for decision_id in ["D-001", "D-002", "D-003", "D-004"]:
            self.assertIn(decision_id, sample)
        self.assertIn("retrospective decision reconstruction", contract)
        self.assertIn("retrospective decision reconstruction", sample)

    def test_evidence_metric_labels_are_updated_everywhere(self):
        integrity = read(REFERENCES / "evidence-integrity.md")
        growth_schema = read(REFERENCES / "growth-file-schema.md")
        template = read(ASSETS / "project-growth-template.md")
        ledger_sample = read(EXAMPLES / "SAMPLE_PRODUCT_DECISION_LOG.md") + "\n" + read(EXAMPLES / "REAL_USE_EVALUATION.md")
        combined = "\n".join([integrity, growth_schema, template, ledger_sample])
        for label in METRIC_LABELS:
            self.assertIn(label, combined)
        for old in ["instrumented metric", "measured result"]:
            self.assertNotIn(old, integrity)

    def test_real_use_evaluation_names_the_regressions_this_version_fixes(self):
        evaluation = read(EXAMPLES / "REAL_USE_EVALUATION.md")
        for phrase in [
            "文件命名不统一",
            "中文输出不够可复制",
            "缺少 decision log",
        ]:
            self.assertIn(phrase, evaluation)


if __name__ == "__main__":
    unittest.main()

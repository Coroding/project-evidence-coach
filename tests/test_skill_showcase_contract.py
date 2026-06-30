import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHOWCASE_DIR = ROOT / "docs" / "skill-showcase"
DATA_PATH = SHOWCASE_DIR / "data" / "showcase-data.json"


class SkillShowcaseContractTest(unittest.TestCase):
    def test_showcase_files_exist(self):
        expected = [
            SHOWCASE_DIR / "index.html",
            SHOWCASE_DIR / "styles.css",
            SHOWCASE_DIR / "app.js",
            DATA_PATH,
        ]

        for path in expected:
            with self.subTest(path=path):
                self.assertTrue(path.exists(), f"Missing showcase file: {path}")

    def test_index_contains_required_static_markers(self):
        index = (SHOWCASE_DIR / "index.html").read_text(encoding="utf-8")

        self.assertIn("Project Evidence Coach", index)
        self.assertTrue(
            "From Repo to Resume" in index or "从项目库到求职材料" in index
        )
        self.assertIn("12 / 16", index)
        self.assertIn("04_PRODUCT_DECISION_LOG.md", index)
        self.assertIn("12_OWNERSHIP_AND_SOURCE_APPENDIX.md", index)

    def test_showcase_data_contract(self):
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))

        for key in [
            "prompt",
            "workflow",
            "repoToResume",
            "outputs",
            "evaluation",
            "iteration",
            "roadmap",
        ]:
            with self.subTest(key=key):
                self.assertIn(key, data)

        repo = data["repoToResume"]["inputProject"]
        self.assertEqual(
            repo["githubUrl"], "https://github.com/Coroding/dont-just-save"
        )
        self.assertEqual(
            repo["githubPagesUrl"], "https://coroding.github.io/dont-just-save/"
        )
        self.assertEqual(repo["vercelUrl"], "https://dont-just-save.vercel.app/")

        self.assertGreaterEqual(len(data["repoToResume"]["resumeOutputs"]), 3)
        self.assertGreaterEqual(len(data["repoToResume"]["portfolioOutline"]), 1)
        self.assertIn("safeClaims", data["repoToResume"]["boundary"])
        self.assertIn("blockedClaims", data["repoToResume"]["boundary"])

        output_files = [item["file"] for item in data["outputs"]["files"]]
        self.assertIn("04_PRODUCT_DECISION_LOG.md", output_files)
        self.assertIn("12_OWNERSHIP_AND_SOURCE_APPENDIX.md", output_files)

        self.assertEqual(data["evaluation"]["total"], 12)
        self.assertEqual(data["evaluation"]["max"], 16)

    def test_css_and_js_interactions(self):
        css = (SHOWCASE_DIR / "styles.css").read_text(encoding="utf-8")
        js = (SHOWCASE_DIR / "app.js").read_text(encoding="utf-8")

        self.assertIn("@media", css)
        self.assertTrue("clipboard.writeText" in js or "copyPrompt" in js)

    def test_readme_links_showcase(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("## Skill Showcase", readme)
        self.assertIn("docs/skill-showcase/index.html", readme)


if __name__ == "__main__":
    unittest.main()

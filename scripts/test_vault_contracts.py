#!/usr/bin/env python3
"""Regression checks for the contract gaps found in the template audit."""
from pathlib import Path
import re
import runpy
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
audit = runpy.run_path(str(ROOT / ".agents/skills/lint-vault/scripts/contracts_audit.py"))["audit"]


class ContractTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for name in ("Type", "Note", "Project", "Responsibility", "Procedure", "Skill"):
            self.write(name.lower() + ".md", f"---\ntype: Type\n---\n# {name}\n")

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def categories(self):
        return {category for category, _, _ in audit(self.root)[0]}

    def pair(self):
        self.write("procedure-example.md", "---\ntype: Procedure\n---\n# Procedure example\n")
        self.write("skills/example.md", '---\ntype: Skill\nstatus: Active\nwraps: "[[procedure-example]]"\npackage_path: ".agents/skills/example/"\n---\n# Example\n')
        self.write(".agents/skills/example/SKILL.md", '---\nname: example\ndescription: "Example workflow"\n---\n# Example\nRead procedure-example.md.\n')

    def test_required_note_contracts(self):
        self.write("plain.md", "# Missing frontmatter\n")
        self.write("heading.md", "---\ntype: Note\n---\n```md\n# Only in code\n```\n")
        self.write("unknown.md", "---\ntype: DoesNotExist\n---\n# Unknown\n")
        self.assertTrue({"frontmatter-missing", "h1-missing", "type-unknown"} <= self.categories())

    def test_copied_project_template_is_complete(self):
        text = (ROOT / "project.md").read_text(encoding="utf-8")
        template = re.search(r"```md\n(.*?)\n```", text, re.S).group(1)
        self.write("first-project.md", template)
        self.assertEqual(self.categories(), set())

    def test_pair_and_procedure_mismatch(self):
        self.pair()
        self.assertEqual(self.categories(), set())
        path = self.root / ".agents/skills/example/SKILL.md"
        path.write_text(path.read_text().replace("name: example", "name: other").replace("procedure-example.md", "different.md"))
        self.assertTrue({"skill-name", "skill-procedure"} <= self.categories())

    def test_missing_package_and_support(self):
        self.pair()
        path = self.root / ".agents/skills/example/SKILL.md"
        original = path.read_text()
        path.write_text(original + "Use `.agents/skills/example/scripts/missing.py`.\n")
        self.assertIn("skill-support-missing", self.categories())
        path.unlink()
        self.assertIn("skill-package-missing", self.categories())

    def test_orphan_and_retired_packages(self):
        self.pair()
        note = self.root / "skills/example.md"
        note.write_text(note.read_text().replace("status: Active", "status: Active\n_archived: true"))
        self.assertTrue({"skill-retired-package", "skill-catalogue"} <= self.categories())

    def test_outside_package_is_not_read(self):
        self.pair()
        (self.root / ".agents/skills/example/SKILL.md").unlink()
        outside = self.root.parent / (self.root.name + "-outside")
        outside.mkdir()
        self.addCleanup(outside.rmdir)
        package = self.root / ".agents/skills/example"
        package.rmdir()
        package.symlink_to(outside, target_is_directory=True)
        self.assertIn("skill-package-path", self.categories())


if __name__ == "__main__":
    unittest.main()

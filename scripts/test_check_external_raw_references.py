#!/usr/bin/env python3
"""Regression checks for unintended disclosure through external Source indexes."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("check_external_raw_references.py")


class ReferenceScopeTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.vault = self.root / "vault"
        self.allowed = self.root / "allowed"
        self.outside = self.root / "outside"
        for folder in (self.vault / ".local", self.allowed, self.outside):
            folder.mkdir(parents=True)
        (self.vault / ".local" / "roots.yml").write_text(
            f'roots:\n  test_files:\n    candidates:\n      - "{self.allowed}"\n',
            encoding="utf-8",
        )

    def note_text(self, relative_path: str) -> str:
        return (
            '---\ntype: Source\nsource_type: "external folder"\n'
            f'root_key: test_files\nrelative_path: "{relative_path}"\n'
            'index_scope: "shallow folder index max depth 2"\n'
            'last_checked: 2000-01-01\n---\n\n# Example source\n'
        )

    def run_checker(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--write", "--date", "2026-01-02"],
            cwd=self.vault,
            capture_output=True,
            text=True,
            check=True,
        )

    def test_unsafe_paths_and_linked_notes_remain_unchanged(self) -> None:
        (self.allowed / "escape").symlink_to(self.outside, target_is_directory=True)
        (self.allowed / "loop").symlink_to("loop")
        cases = {
            "absolute.md": str(self.outside),
            "parent.md": "../outside",
            "symlink.md": "escape",
            "loop.md": "loop",
        }
        originals = {}
        for name, relative in cases.items():
            path = self.vault / name
            originals[path] = self.note_text(relative)
            path.write_text(originals[path], encoding="utf-8")

        linked_note = self.outside / "linked-note.md"
        originals[linked_note] = self.note_text(".")
        linked_note.write_text(originals[linked_note], encoding="utf-8")
        (self.vault / "linked.md").symlink_to(linked_note)
        result = self.run_checker()

        for path, original in originals.items():
            with self.subTest(path=path.name):
                self.assertEqual(path.read_text(encoding="utf-8"), original)
        self.assertEqual(result.stdout.count("WARN unsafe or unresolvable relative_path"), 4)
        self.assertNotIn(str(self.root), result.stdout)

    def test_valid_indexes_refresh_without_following_directory_symlinks(self) -> None:
        project = self.allowed / "project"
        visible = project / "visible"
        (visible / "nested").mkdir(parents=True)
        (project / "outside-link").symlink_to(self.outside, target_is_directory=True)
        (visible / "outside-nested-link").symlink_to(self.outside, target_is_directory=True)
        (self.allowed / "alias").symlink_to(project, target_is_directory=True)
        for name, relative in (("direct.md", "project"), ("alias.md", "alias")):
            (self.vault / name).write_text(self.note_text(relative), encoding="utf-8")

        result = self.run_checker()

        for name in ("direct.md", "alias.md"):
            with self.subTest(path=name):
                updated = (self.vault / name).read_text(encoding="utf-8")
                self.assertIn("last_checked: 2026-01-02", updated)
                self.assertIn("- `visible`", updated)
                self.assertIn("  - `nested`", updated)
                self.assertNotIn("outside-link", updated)
                self.assertNotIn("outside-nested-link", updated)
        self.assertNotIn(str(self.root), result.stdout)
        self.assertIn("vault notes needing update: 2", result.stdout)

    def test_archived_source_is_not_checked_or_rewritten(self) -> None:
        path = self.vault / "archived.md"
        original = self.note_text(".").replace("type: Source", "type: Source\n_archived: true")
        path.write_text(original, encoding="utf-8")
        result = self.run_checker()
        self.assertEqual(path.read_text(encoding="utf-8"), original)
        self.assertNotIn("archived.md", result.stdout)
        self.assertIn("vault notes needing update: 0", result.stdout)


if __name__ == "__main__":
    unittest.main()

"""Distribution checks; behavioral outcomes are evaluated separately in evals/."""
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
from urllib.parse import unquote, urlsplit

from skills_ref import read_properties, validate
from strictyaml import load


ROOT = Path(__file__).resolve().parents[1]
NAMES = {"record-knowledge", "curate-knowledge", "continue-work"}


class DistributionTests(unittest.TestCase):
    def check_links(self, root):
        for path in root.rglob("*.md"):
            if any(part in {".git", ".venv", "fixtures"} for part in path.parts):
                continue
            fence = None
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.startswith(("```", "~~~")):
                    marker = line[:3]
                    fence = None if fence == marker else marker
                    continue
                if fence:
                    continue
                # shortcut: inline links only; use a Markdown parser if reference-style links are introduced.
                for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", line):
                    url = urlsplit(target.strip("<>"))
                    if url.scheme or url.netloc or not url.path:
                        continue
                    destination = (path.parent / unquote(url.path)).resolve()
                    with self.subTest(file=str(path), target=target):
                        self.assertTrue(destination.is_relative_to(root.resolve()),
                                        "Local link escapes the distributed package")
                        self.assertTrue(destination.exists(), "Missing local link target")

    def test_skills_are_independently_installable(self):
        sources = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual({p.parent.name for p in sources}, NAMES)
        for source in sources:
            with self.subTest(skill=source.parent.name), tempfile.TemporaryDirectory() as tmp:
                package = Path(tmp) / source.parent.name
                shutil.copytree(source.parent, package)
                self.assertEqual(validate(package), [])
                props = read_properties(package)
                self.assertEqual(props.name, package.name)
                self.assertEqual((package / "LICENSE").read_bytes(),
                                 (ROOT / "LICENSE").read_bytes())
                metadata = load((package / "agents/openai.yaml").read_text()).data
                interface = metadata["interface"]
                self.assertTrue(interface["display_name"])
                self.assertTrue(25 <= len(interface["short_description"]) <= 64)
                self.assertIn(f"${props.name}", interface["default_prompt"])
                self.check_links(package)

    def test_repository_links(self):
        self.check_links(ROOT)

    def test_repository_discovery_uses_the_same_skills(self):
        for name in NAMES:
            with self.subTest(skill=name):
                local = ROOT / ".agents/skills" / name
                self.assertTrue(local.is_symlink())
                self.assertEqual(local.resolve(), (ROOT / "skills" / name).resolve())

    def test_scheduler_fixture_is_read_only_and_consistent(self):
        import json
        import sys
        fixture = ROOT / "evals/fixtures/resume/tools/job_status.py"
        before = fixture.read_bytes()
        result = subprocess.run([sys.executable, str(fixture)], check=True,
                                capture_output=True, text=True)
        status = json.loads(result.stdout)
        completed = set(status["completed_shards"])
        remaining = set(status["remaining_shards"])
        self.assertFalse(completed & remaining)
        self.assertEqual(completed | remaining, set(range(4)))
        self.assertEqual(status["status"], "RUNNING")
        self.assertEqual(fixture.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()

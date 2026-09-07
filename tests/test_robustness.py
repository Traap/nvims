"""Offline regression checks: python3 -m unittest discover -s tests -v."""
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class RobustnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="nvims-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        self.config = self.root / ".config/nvims"
        self.config.mkdir(parents=True)
        (self.config / "neovim_distros").write_text(
            (ROOT / "neovim_distros").read_text()
        )

    def launch(self, choice, git_status=0, flags="", git_body=None):
        # Substitute paths without changing the test runner's HOME.
        source = (ROOT / "nvims").read_text().replace("$HOME", str(self.root))
        source = source.rsplit('main "$@"', 1)[0]
        body = git_body or f'return {git_status}'
        mocks = f'''
        fzf() {{ cat >/dev/null; printf '%s\\n' '{choice}'; }}
        git() {{ printf 'git %s\\n' "$*" >>'{self.root}/git.log'; {body}; }}
        nvim() {{ printf '%s' "$NVIM_APPNAME" >'{self.root}/launched'; }}
        {flags}
        main
        '''
        return subprocess.run(["bash", "-c", source + mocks], capture_output=True, text=True)

    def test_failed_clone_does_not_publish_or_launch(self):
        result = self.launch("astro", 1, "setDefaultFlag=true")
        self.assertNotEqual(result.returncode, 0)
        for name in ("nvim_appnames", "nvim_default_app"):
            self.assertFalse((self.config / name).exists())
        self.assertFalse((self.root / "launched").exists())

    def test_plain_default_never_calls_git(self):
        result = self.launch("default", 1)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.root / "git.log").exists())
        self.assertEqual((self.root / "launched").read_text(), "nvim-default")

    def test_stale_default_stops_before_mutation(self):
        (self.config / "nvim_default_app").write_text("removed-distro")
        result = self.launch("default")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / "git.log").exists())
        self.assertFalse((self.config / "nvim_appnames").exists())
        self.assertFalse((self.root / "launched").exists())

    def test_failed_pull_does_not_launch(self):
        (self.root / ".config/nvim-astro").mkdir()
        result = self.launch("astro", git_body='[[ $1 != pull ]]')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / "launched").exists())

    def test_failed_checkout_does_not_launch(self):
        (self.root / ".config/nvim-whiskey").mkdir()
        result = self.launch("whiskey", git_body='[[ $1 != checkout ]]')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / "launched").exists())

    def test_pinned_commit_launches_without_pull(self):
        (self.root / ".config/nvim-whiskey").mkdir()
        result = self.launch("whiskey", git_body='[[ $1 != symbolic-ref ]]')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("git pull", (self.root / "git.log").read_text())
        self.assertTrue((self.root / "launched").exists())

    def test_success_publishes_default_and_alias(self):
        result = self.launch("astro", flags="setDefaultFlag=true")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.config / "nvim_default_app").read_text(), "astro\n")
        self.assertIn("alias nvim-astro=", (self.config / "nvim_appnames").read_text())
        self.assertTrue((self.root / "launched").exists())

    def test_failed_install_stops_and_cleans_private_directory(self):
        checkout = self.root / "checkout"
        checkout.mkdir()
        marker = self.root / "sudo-called"
        mocks = f'''
        mktemp() {{ printf '%s\\n' '{checkout}'; }}
        git() {{ return 1; }}
        sudo() {{ touch '{marker}'; }}
        '''
        result = subprocess.run(
            ["bash", "-c", mocks + (ROOT / "install.sh").read_text()],
            capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(marker.exists())
        self.assertFalse(checkout.exists())
        self.assertNotIn("Installation complete.", result.stdout)


if __name__ == "__main__":
    unittest.main()

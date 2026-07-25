import subprocess
import sys
from pathlib import Path


def test_main_prints_project_greeting():
    project_root = Path(__file__).parents[1]
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=project_root,
        capture_output=True,
        check=True,
        text=True,
    )

    assert result.stdout == "Hello from scan-vuln!\n"

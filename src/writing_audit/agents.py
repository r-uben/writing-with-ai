from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def run_agent(agent: str, prompt: str, out: Path) -> bool:
    """Invoke an external CLI agent; return False if unavailable or failed."""
    exe = shutil.which(agent)
    if exe is None:
        return False

    if agent == "claude":
        cmd = [exe, "-p", prompt]
    elif agent == "codex":
        cmd = [exe, "exec", "--skip-git-repo-check", prompt]
    elif agent == "agy":
        cmd = [exe, "-p", prompt]
    else:
        raise ValueError(f"Unknown agent: {agent}")

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return False
    out.write_text(result.stdout)
    return True

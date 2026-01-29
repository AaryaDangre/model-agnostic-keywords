import os
from pathlib import Path


def test_compile_creates_outputs():
    root = Path(__file__).resolve().parents[1]
    script = root / "scripts" / "compile_keywords.py"
    assert script.exists(), "compile_keywords.py missing"

    # run the script
    import subprocess
    subprocess.check_call(["python", "-m", "scripts.compile_keywords"], cwd=str(root))

    out_json = root / "prompt-keywords" / "combined_keywords.json"
    out_yaml = root / "prompt-keywords" / "combined_keywords.yml"

    assert out_json.exists(), "combined_keywords.json was not created"
    assert out_json.stat().st_size > 0

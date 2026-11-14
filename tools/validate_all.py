#!/usr/bin/env python3
"""
tools/validate_all.py

Comprehensive Validation Suite for Dhanush M D's GitHub Profile Architecture.
Validates:
1. Local image paths referenced in README.md.
2. XML parsing and well-formedness of all SVGs in assets/.
3. Execution and exit codes of build and generation scripts.
4. Unit tests in scripts/test_activity_graph.py.
5. GitHub Actions workflow syntax and structure.
6. Verification that no secret leaks or unreplaced placeholders exist.
"""

import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_readme_local_links():
    print("[1/6] Checking local file paths referenced in README.md...")
    readme_path = os.path.join(REPO_ROOT, "README.md")
    assert os.path.exists(readme_path), "README.md missing!"

    content = open(readme_path, encoding="utf-8").read()
    # Match src="assets/..."
    local_images = re.findall(r'src=["\'](assets/[^"\']+)["\']', content)
    for img in local_images:
        full_p = os.path.join(REPO_ROOT, img.replace("/", os.sep))
        if not os.path.exists(full_p):
            raise AssertionError(f"Referenced asset does not exist: {img} -> {full_p}")
        print(f"  [PASS] Found asset: {img}")
    print(f"  All {len(local_images)} local image references verified.")

def test_svg_xml_validity():
    print("\n[2/6] Validating all SVG files in assets/...")
    count = 0
    for root, dirs, files in os.walk(os.path.join(REPO_ROOT, "assets")):
        for f in files:
            if f.endswith(".svg"):
                full_p = os.path.join(root, f)
                try:
                    ET.parse(full_p)
                    count += 1
                except ET.ParseError as e:
                    raise AssertionError(f"Invalid XML in {full_p}: {e}")
    print(f"  All {count} SVG files are valid XML.")

def test_python_scripts():
    print("\n[3/6] Running asset build and generator scripts...")
    scripts = [
        ("tools/build_assets.py", ["python", "tools/build_assets.py"]),
        ("scripts/generate_hero.py", ["python", "scripts/generate_hero.py"]),
        ("scripts/generate_activity_graph.py", ["python", "scripts/generate_activity_graph.py", "--from-json"]),
    ]
    for name, cmd in scripts:
        res = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        if res.returncode != 0:
            print(res.stdout)
            print(res.stderr)
            raise AssertionError(f"Script failed with code {res.returncode}: {name}")
        print(f"  [PASS] {name} executed successfully.")

def test_unit_tests():
    print("\n[4/6] Running unit tests...")
    cmd = ["python", "-m", "unittest", "scripts/test_activity_graph.py"]
    res = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stdout)
        print(res.stderr)
        raise AssertionError("Unit tests failed!")
    print(f"  [PASS] All unit tests passed:\n{res.stderr.strip()}")

def test_workflow_file():
    print("\n[5/6] Checking GitHub Actions workflow...")
    wf = os.path.join(REPO_ROOT, ".github", "workflows", "update-activity.yml")
    assert os.path.exists(wf), "Workflow file missing!"
    content = open(wf, encoding="utf-8").read()
    assert "cron:" in content, "Workflow missing cron schedule!"
    assert "workflow_dispatch:" in content, "Workflow missing workflow_dispatch trigger!"
    assert "GH_TOKEN:" in content, "Workflow missing GH_TOKEN secret reference!"
    assert "update-activity" in content or "update-graph" in content
    print("  [PASS] Workflow structure verified.")

def test_no_forbidden_placeholders():
    print("\n[6/6] Verifying no raw placeholders or secret exposures...")
    forbidden = ["YOUR_USERNAME", "YOUR_EMAIL", "REPLACE_ME", "TODO_NAME", "ghp_", "github_pat_"]
    checked_files = [
        "README.md",
        "scripts/generate_activity_graph.py",
        "tools/build_assets.py",
        ".github/workflows/update-activity.yml",
    ]
    for rel_p in checked_files:
        full_p = os.path.join(REPO_ROOT, rel_p)
        content = open(full_p, encoding="utf-8").read()
        for term in forbidden:
            assert term not in content, f"Forbidden placeholder '{term}' found in {rel_p}!"
    print("  [PASS] No placeholders or credential leaks found.")

if __name__ == "__main__":
    print("=== DHANUSH M D PROFILE VALIDATION SUITE ===")
    test_readme_local_links()
    test_svg_xml_validity()
    test_python_scripts()
    test_unit_tests()
    test_workflow_file()
    test_no_forbidden_placeholders()
    print("\n============================================")
    print("ALL VALIDATION CHECKS PASSED WITH 100% SUCCESS.")
    print("============================================")


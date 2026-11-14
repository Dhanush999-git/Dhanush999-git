#!/usr/bin/env python3
"""
scripts/generate_hero.py

Generates the custom Cyber Obsidian × Electric Prismatic Hero Banner for Dhanush M D.
Outputs to assets/hero/hero-banner.svg and assets/hero-banner.svg
"""

import os
import sys

# Add repository root to path
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from tools.build_assets import generate_hero_banner, validate_svg

def main():
    svg_content = generate_hero_banner()
    p1 = os.path.join(REPO_ROOT, "assets", "hero", "hero-banner.svg")
    p2 = os.path.join(REPO_ROOT, "assets", "hero-banner.svg")
    validate_svg(svg_content, p1)
    validate_svg(svg_content, p2)
    print("Hero banner successfully regenerated.")

if __name__ == "__main__":
    main()


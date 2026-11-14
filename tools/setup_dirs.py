import os

dirs = [
    "assets/hero",
    "assets/sections",
    "assets/badges",
    "assets/cards",
    "assets/activity",
    "scripts",
    "tools",
    ".github/workflows",
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Created {d}")


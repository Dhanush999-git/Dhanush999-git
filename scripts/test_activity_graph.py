#!/usr/bin/env python3
"""
scripts/test_activity_graph.py

Unit tests for generate_activity_graph.py and asset generation.
Verifies date continuity, weekday calculation, level mapping,
calendar validation, stats aggregation, and valid XML output.
"""

import copy
import json
import os
import sys
import unittest
import xml.etree.ElementTree as ET
from datetime import date, timedelta

# Add scripts directory to path
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)
sys.path.insert(0, SCRIPTS_DIR)

import generate_activity_graph as act

class TestActivityGraph(unittest.TestCase):

    def test_gh_weekday(self):
        # Sunday should be 0
        sun = date(2026, 11, 15)  # 2026-11-15 is Sunday
        self.assertEqual(act.gh_weekday(sun), 0)
        # Monday should be 1
        mon = date(2026, 11, 16)
        self.assertEqual(act.gh_weekday(mon), 1)
        # Saturday should be 6
        sat = date(2026, 11, 14)
        self.assertEqual(act.gh_weekday(sat), 6)

    def test_create_fallback_calendar(self):
        cal = act.create_fallback_calendar(today=date(2026, 11, 15))
        self.assertTrue(act.validate_calendar(cal))
        self.assertEqual(cal["username"], act.USERNAME)
        self.assertGreater(len(cal["days"]), 360)
        # First day should be Sunday
        first_d = date.fromisoformat(cal["days"][0]["date"])
        self.assertEqual(act.gh_weekday(first_d), 0)

    def test_validate_calendar_gap_detected(self):
        cal = act.create_fallback_calendar(today=date(2026, 11, 15))
        # Remove a day to create a gap
        del cal["days"][50]
        with self.assertRaises(act.ValidationError):
            act.validate_calendar(cal)

    def test_calculate_stats(self):
        cal = act.create_fallback_calendar(today=date(2026, 11, 15))
        stats = act.calculate_stats(cal)
        self.assertIn("total", stats)
        self.assertIn("active_days", stats)
        self.assertIn("longest_streak", stats)
        self.assertIn("current_streak", stats)
        self.assertGreaterEqual(stats["total"], 0)

    def test_render_svg_valid_xml(self):
        cal = act.create_fallback_calendar(today=date(2026, 11, 15))
        svg_str = act.render_svg(cal)
        # Verify valid XML parse
        root = ET.fromstring(svg_str)
        self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
        self.assertEqual(root.attrib.get("viewBox"), "0 0 1000 240")

    def test_color_level_mapping(self):
        self.assertEqual(act.LEVEL_MAP["NONE"], 0)
        self.assertEqual(act.LEVEL_MAP["FIRST_QUARTILE"], 1)
        self.assertEqual(act.LEVEL_MAP["SECOND_QUARTILE"], 2)
        self.assertEqual(act.LEVEL_MAP["THIRD_QUARTILE"], 3)
        self.assertEqual(act.LEVEL_MAP["FOURTH_QUARTILE"], 4)
        for i in range(5):
            self.assertIn(i, act.COLORS)
            self.assertTrue(act.COLORS[i].startswith("#"))

if __name__ == "__main__":
    unittest.main()


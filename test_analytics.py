
import unittest
from analytics import (
    longest_daily_streak,
    longest_weekly_streak,
    longest_streak_duration,
)


class TestAnalytics(unittest.TestCase):

    def test_longest_daily_streak(self):
        completions = [
            "2026-10-20 08:00:00",
            "2026-10-21 08:00:00",
            "2026-10-22 08:00:00",
            "2026-10-24 08:00:00",
        ]
        self.assertEqual(longest_daily_streak(completions), 3)

    def test_empty_daily_history(self):
        self.assertEqual(longest_daily_streak([]), 0)

    def test_one_daily_completion(self):
        completions = ["2026-10-25 08:00:00"]
        self.assertEqual(longest_daily_streak(completions), 1)

    def test_longest_weekly_streak(self):
        completions = [
            "2026-10-05 08:00:00",
            "2026-10-12 08:00:00",
            "2026-10-19 08:00:00",
            "2026-11-02 08:00:00",
        ]
        self.assertEqual(longest_weekly_streak(completions), 3)

    def test_empty_weekly_history(self):
        self.assertEqual(longest_weekly_streak([]), 0)


    def test_daily_streak_duration(self):
        completions = [
            "2026-10-01 08:00:00",
            "2026-10-02 08:00:00",
            "2026-10-03 08:00:00",
            "2026-10-04 08:00:00",
        ]
        self.assertEqual(
            longest_streak_duration(completions, "daily"), 3
        )

    def test_weekly_streak_duration(self):
        completions = [
            "2026-10-05 08:00:00",
            "2026-10-12 08:00:00",
            "2026-10-19 08:00:00",
            "2026-10-26 08:00:00",
        ]
        self.assertEqual(
            longest_streak_duration(completions, "weekly"), 21
        )

    def test_empty_streak_duration(self):
        self.assertEqual(longest_streak_duration([], "daily"), 0)

    def test_single_completion_duration(self):
        completions = ["2026-10-01 08:00:00"]
        self.assertEqual(
            longest_streak_duration(completions, "daily"), 0
        )


if __name__ == "__main__":
    unittest.main()

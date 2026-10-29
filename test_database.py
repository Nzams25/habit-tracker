
import unittest
import os
from database import HabitTracker
from habit import Habit


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database_name = "test_habits.db"

        if os.path.exists(self.database_name):
            os.remove(self.database_name)

        self.tracker = HabitTracker(self.database_name)

    def tearDown(self):
        self.tracker.connection.close()

        if os.path.exists(self.database_name):
            os.remove(self.database_name)

    def test_add_habit(self):
        habit = Habit("Read for 20 minutes", "daily")
        self.tracker.add_habit(habit)

        result = self.tracker.connection.execute(
            "SELECT name, periodicity, created_at FROM habits"
        ).fetchone()

        self.assertEqual(result[0], "Read for 20 minutes")
        self.assertEqual(result[1], "daily")
        self.assertEqual(result[2], habit.created_at)

    def test_get_all_habits(self):
        habit1 = Habit("Read for 20 minutes", "daily")
        habit2 = Habit("Exercise", "weekly")

        self.tracker.add_habit(habit1)
        self.tracker.add_habit(habit2)

        habits = self.tracker.get_all_habits()

        self.assertEqual(len(habits), 2)
        self.assertEqual(habits[0][1], "Read for 20 minutes")
        self.assertEqual(habits[1][1], "Exercise")
        self.assertEqual(habits[0][2], "daily")
        self.assertEqual(habits[1][2], "weekly")


    def test_add_completion(self):
        habit = Habit("Read for 20 minutes", "daily")
        self.tracker.add_habit(habit)

        result = self.tracker.connection.execute(
            "SELECT id FROM habits WHERE name = ?",
            ("Read for 20 minutes",)
        ).fetchone()

        habit_id = result[0]
        completed_at = "2026-10-23 05:15:00"

        self.tracker.add_completion(habit_id, completed_at)

        completion = self.tracker.connection.execute(
            """
            SELECT habit_id, completed_at
            FROM completions
            WHERE habit_id = ?
            """,
            (habit_id,)
        ).fetchone()

        self.assertEqual(completion[0], habit_id)
        self.assertEqual(completion[1], completed_at)


    def test_get_completions(self):
        habit = Habit("Read for 20 minutes", "daily")
        self.tracker.add_habit(habit)

        result = self.tracker.connection.execute(
            "SELECT id FROM habits WHERE name = ?",
            ("Read for 20 minutes",)
        ).fetchone()

        habit_id = result[0]

        self.tracker.add_completion(
            habit_id, "2026-10-21 08:00:00"
        )
        self.tracker.add_completion(
            habit_id, "2026-10-22 08:15:00"
        )

        completions = self.tracker.get_completions(habit_id)

        self.assertEqual(len(completions), 2)
        self.assertEqual(completions,["2026-10-21 08:00:00", "2026-10-22 08:15:00"])


    def test_delete_habit(self):
        habit = Habit("Read for 20 minutes", "daily")
        self.tracker.add_habit(habit)

        result = self.tracker.connection.execute(
            "SELECT id FROM habits WHERE name = ?",
            ("Read for 20 minutes",)
        ).fetchone()

        habit_id = result[0]

        self.tracker.add_completion(
            habit_id, "2026-10-23 08:00:00"
        )

        self.tracker.delete_habit(habit_id)

        remaining_habit = self.tracker.connection.execute(
            "SELECT id FROM habits WHERE id = ?",
            (habit_id,)
        ).fetchone()

        remaining_completions = self.tracker.connection.execute(
            "SELECT id FROM completions WHERE habit_id = ?",
            (habit_id,)
        ).fetchall()

        self.assertIsNone(remaining_habit)
        self.assertEqual(remaining_completions, [])


if __name__ == "__main__":
    unittest.main()







import unittest
from habit import Habit


class TestHabit(unittest.TestCase):

    def test_create_daily_habit(self):
        my_habit = Habit("Read for 20 minutes", "daily")

        self.assertEqual(my_habit.name, "Read for 20 minutes")
        self.assertEqual(my_habit.periodicity, "daily")


    def test_create_weekly_habit(self):
        my_habit = Habit("Exercise", "weekly")

        self.assertEqual(my_habit.name, "Exercise")
        self.assertEqual(my_habit.periodicity, "weekly")


    def test_empty_habit_name(self):
        with self.assertRaises(ValueError):
            Habit("", "daily")


    def test_habit_name_with_spaces(self):
        with self.assertRaises(ValueError):
            Habit("   ", "daily")


    def test_invalid_periodicity(self):
        with self.assertRaises(ValueError):
            Habit("Exercise", "monthly")


    def test_complete_habit(self):
        my_habit = Habit("Read for 20 minutes", "daily")

        completed_at = my_habit.complete_habit()

        self.assertIn(completed_at, my_habit.completions)
        self.assertEqual(len(my_habit.completions), 1)


    def test_multiple_completions(self):
        my_habit = Habit("Read for 20 minutes", "daily")

        my_habit.complete_habit()
        my_habit.complete_habit()

        self.assertEqual(len(my_habit.completions), 2)


    def test_creation_timestamp(self):
        my_habit = Habit("Exercise", "daily")

        self.assertIsNotNone(my_habit.created_at)
        self.assertNotEqual(my_habit.created_at, "")



    def test_completion_timestamp(self):
        my_habit = Habit("Exercise", "daily")

        completed_at = my_habit.complete_habit()

        self.assertIsInstance(completed_at, str)
        self.assertNotEqual(completed_at, "")



    def test_show_habit(self):
        my_habit = Habit("Exercise", "daily")

        my_habit.complete_habit()

        my_habit.show_habit()




if __name__ == "__main__":
    unittest.main()

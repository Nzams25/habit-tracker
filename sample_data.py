
from habit import Habit


def load_sample_data(tracker):
    """Add predefined habits and four weeks of sample completions."""

    sample_habits = [
        ("Read for 20 minutes", "daily"),
        ("Exercise", "weekly"),
        ("Study Python", "daily"),
        ("Drink water", "daily"),
        ("Plan the week", "weekly"),
    ]

    for name, periodicity in sample_habits:
        existing_habits = tracker.get_all_habits()

        if any(habit[1] == name for habit in existing_habits):
            print(f"'{name}' already exists. Skipping.")
            continue

        habit = Habit(name, periodicity)
        habit_id = tracker.add_habit(habit)

        print(f"Added sample habit: {name}")


    # Add four weeks of sample completion records.
    from datetime import datetime, timedelta

    today = datetime.now().date()

    for name, periodicity in sample_habits:
        existing_habits = tracker.get_all_habits()

        for saved_habit in existing_habits:
            if saved_habit[1] == name:
                habit_id = saved_habit[0]
                break

        else:
            continue

        number_of_weeks = 4

        if periodicity == "daily":
            number_of_completions = 28
            interval_days = 1
        else:
            number_of_completions = 4
            interval_days = 7

        existing_completions = tracker.get_completions(habit_id)

        if existing_completions:
            print(f"'{name}' already has completions. Skipping sample records.")
            continue

        for index in range(number_of_completions):
            completion_date = today - timedelta(
                days=interval_days * (number_of_completions - 1 - index)
            )

            completed_at = datetime.combine(
                completion_date, datetime.min.time()
            ).strftime("%Y-%m-%d %H:%M:%S")

            tracker.add_completion(habit_id, completed_at)

        print(f"Added sample completions for: {name}")

    print("Sample data loading finished.")


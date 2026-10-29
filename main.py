
from database import HabitTracker
from habit import Habit
from datetime import datetime
from sample_data import load_sample_data
from analytics import (
    longest_daily_streak,
    longest_weekly_streak,
    longest_streak_duration,
)


def main():
    """Display the main menu."""

    tracker = HabitTracker()

    try:
        while True:
            print("\n##### WELCOME TO MY HABIT TRACKER #####")
            print("\nMAIN MENU")
            print("1. Create a habit")
            print("2. View all habits")
            print("3. Mark a habit as complete")
            print("4. View one habit")
            print("5. Delete a habit")
            print("6. View daily habits")
            print("7. View weekly habits")
            print("8. View longest streak across all habits")
            print("9. View longest streak for one habit")
            print("10. Load predefined sample data")
            print("0. Exit")

            choice = input("\nChoose an option: ").strip()

            if choice == "0":
                print("Thank you for using Habit Tracker!")
                break


            elif choice == "1":

                name = input("Enter habit name: ").strip()

                periodicity = input("Enter periodicity (daily/weekly): ").strip().lower()

                try:

                    habit = Habit(name, periodicity)

                    habit_id = tracker.add_habit(habit)

                    print(f"Habit created successfully! Its ID is {habit_id}.")


                except ValueError as error:

                    print(f"Error: {error}")



            elif choice == "2":

                habits = tracker.get_all_habits()

                if not habits:

                    print("No habits found.")

                else:

                    print("\nYour habits:")

                    for habit in habits:
                        print(f"ID: {habit[0]}")

                        print(f"Name: {habit[1]}")

                        print(f"Periodicity: {habit[2]}")

                        print(f"Created at: {habit[3]}")

                        print("-" * 30)



            elif choice == "3":

                try:

                    habit_id = int(input("Enter the habit ID: "))

                    habits = tracker.get_all_habits()

                    habit_ids = [habit[0] for habit in habits]

                    if habit_id not in habit_ids:

                        print("Habit ID not found.")

                    else:

                        completed_at = datetime.now().strftime(

                            "%Y-%m-%d %H:%M:%S"

                        )

                        tracker.add_completion(habit_id, completed_at)

                        print(f"Habit completed at {completed_at}.")


                except ValueError:

                    print("Please enter a valid numeric habit ID.")



            elif choice == "4":

                try:

                    habit_id = int(input("Enter the habit ID: "))

                    habits = tracker.get_all_habits()

                    selected_habit = None

                    for habit in habits:

                        if habit[0] == habit_id:
                            selected_habit = habit

                            break

                    if selected_habit is None:

                        print("Habit ID not found.")

                    else:

                        print("\nHabit details:")

                        print(f"ID: {selected_habit[0]}")

                        print(f"Name: {selected_habit[1]}")

                        print(f"Periodicity: {selected_habit[2]}")

                        print(f"Created at: {selected_habit[3]}")

                        completions = tracker.get_completions(habit_id)

                        if completions:

                            print("Completion history:")

                            for completion in completions:
                                print(completion)

                        else:

                            print("No completion records yet.")


                except ValueError:

                    print("Please enter a valid numeric habit ID.")



            elif choice == "5":

                try:

                    habit_id = int(input("Enter the habit ID to delete: "))

                    habits = tracker.get_all_habits()

                    habit_ids = [habit[0] for habit in habits]

                    if habit_id not in habit_ids:

                        print("Habit ID not found.")

                    else:

                        tracker.delete_habit(habit_id)

                        print(f"Habit with ID {habit_id} deleted successfully.")


                except ValueError:

                    print("Please enter a valid numeric habit ID.")




            elif choice == "6":

                habits = tracker.get_all_habits()

                daily_habits = [

                    habit for habit in habits

                    if habit[2] == "daily"

                ]

                if not daily_habits:

                    print("No daily habits found.")

                else:

                    print("\nYour daily habits:")

                    for habit in daily_habits:
                        print(f"ID: {habit[0]}")

                        print(f"Name: {habit[1]}")

                        print(f"Periodicity: {habit[2]}")

                        print(f"Created at: {habit[3]}")

                        print("-" * 30)



            elif choice == "7":

                habits = tracker.get_all_habits()

                weekly_habits = [

                    habit for habit in habits

                    if habit[2] == "weekly"

                ]

                if not weekly_habits:

                    print("No weekly habits found.")

                else:

                    print("\nYour weekly habits:")

                    for habit in weekly_habits:
                        print(f"ID: {habit[0]}")

                        print(f"Name: {habit[1]}")

                        print(f"Periodicity: {habit[2]}")

                        print(f"Created at: {habit[3]}")

                        print("-" * 30)


            elif choice == "8":

                habits = tracker.get_all_habits()

                if not habits:

                    print("No habits found.")

                else:

                    longest_duration = -1

                    longest_habit_name = None

                    longest_periodicity = None

                    for habit in habits:

                        habit_id = habit[0]

                        habit_name = habit[1]

                        periodicity = habit[2]

                        completions = tracker.get_completions(habit_id)

                        duration = longest_streak_duration(

                            completions, periodicity

                        )

                        if duration > longest_duration:
                            longest_duration = duration

                            longest_habit_name = habit_name

                            longest_periodicity = periodicity

                    if longest_duration == 0:

                        print("No streak duration recorded yet.")

                    else:

                        print("\nLongest streak across all habits:")

                        print(f"Habit: {longest_habit_name}")

                        print(f"Periodicity: {longest_periodicity}")

                        print(

                            f"Longest streak duration: "

                            f"{longest_duration} calendar days"

                        )



            elif choice == "9":

                try:

                    habit_id = int(input("Enter the habit ID: "))

                    habits = tracker.get_all_habits()

                    selected_habit = None

                    for habit in habits:

                        if habit[0] == habit_id:
                            selected_habit = habit

                            break

                    if selected_habit is None:

                        print("Habit ID not found.")

                    else:

                        habit_name = selected_habit[1]

                        periodicity = selected_habit[2]

                        completions = tracker.get_completions(habit_id)

                        if periodicity == "daily":

                            streak = longest_daily_streak(completions)

                            period_name = "days"

                        else:

                            streak = longest_weekly_streak(completions)

                            period_name = "weeks"

                        print("\nLongest streak for this habit:")

                        print(f"Habit: {habit_name}")

                        print(f"Periodicity: {periodicity}")

                        print(f"Longest streak: {streak} {period_name}")


                except ValueError:

                    print("Please enter a valid numeric habit ID.")



            elif choice == "10":

                load_sample_data(tracker)



            else:
                print("Invalid choice. Please try again.")

    finally:
        tracker.connection.close()


if __name__ == "__main__":
    main()





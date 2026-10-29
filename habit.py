from datetime import datetime

"""Represent a habit and track its completion history"""
class Habit:
    def __init__(self, name, periodicity, created_at=None):
        if not name.strip():
            raise ValueError("Habit name should not be left empty")

        if periodicity not in ("daily", "weekly"):
            raise ValueError("'daily' or 'weekly' should be the only periodicity")

        self.name = name
        self.periodicity = periodicity

        if created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.created_at = created_at

        self.completions = []

    def show_habit(self):
        print(f"Habit: {self.name}")
        print(f"Periodicity: {self.periodicity}")
        print(f"Created at: {self.created_at}")

        if self.completions:
            print("Completion history")
            for completion in self.completions:
                print(completion)

        else:
            print("There is no completion record yet")

    def complete_habit(self):
        completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completions.append(completed_at)

        return completed_at





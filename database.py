import sqlite3
from habit import Habit

class HabitTracker:
    """Manage habits and their completion records in SQLite."""

    def __init__(self, database_name="habits.db"):
        self.connection = sqlite3.connect(database_name)
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.create_tables()

    def create_tables(self):
        """Create the database tables if they do not exist."""
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                periodicity TEXT NOT NULL
                    CHECK (periodicity IN ('daily', 'weekly')),
                created_at TEXT NOT NULL
            )
        """)

        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS completions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER NOT NULL,
                completed_at TEXT NOT NULL,
                FOREIGN KEY (habit_id)
                    REFERENCES habits(id)
                    ON DELETE CASCADE
            )
        """)

        self.connection.commit()

    def add_habit(self, habit):
        """Save a habit to the database and return its ID."""
        cursor = self.connection.execute(
            """INSERT INTO habits (name, periodicity, created_at)
               VALUES (?, ?, ?)""",
            (habit.name, habit.periodicity, habit.created_at)
        )
        self.connection.commit()
        return cursor.lastrowid

    def get_all_habits(self):
        """Retrieve all saved habits from the database."""
        cursor = self.connection.execute(
            """
            SELECT id, name, periodicity, created_at
            FROM habits
            ORDER BY id
            """
        )
        return cursor.fetchall()


    def add_completion(self, habit_id, completed_at):
        """Save a habit completion to the database."""
        self.connection.execute(
            """
            INSERT INTO completions (habit_id, completed_at)
            VALUES (?, ?)
            """,
            (habit_id, completed_at)
        )
        self.connection.commit()


    def get_completions(self, habit_id):
        """Retrieve completion timestamps for a specific habit."""
        cursor = self.connection.execute(
            """
            SELECT completed_at
            FROM completions
            WHERE habit_id = ?
            ORDER BY completed_at
            """,
            (habit_id,)
        )
        return [row[0] for row in cursor.fetchall()]


    def delete_habit(self, habit_id):
        """Delete a habit and its completion records."""
        self.connection.execute(
            "DELETE FROM habits WHERE id = ?",
            (habit_id,)
        )
        self.connection.commit()




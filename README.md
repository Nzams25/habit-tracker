# Habit Tracker

## 1. Project Overview

Habit Tracker is a command-line application developed in Python to help users create, manage, and monitor their daily and weekly habits.

The application allows users to record habit completions, review their completion history, and analyse their consistency over time. It uses an SQLite database to store habits and completion records, allowing information to remain available when the application is closed and restarted.

This project demonstrates object-oriented programming, database management, functional-style data analysis, input validation, exception handling, and automated testing in Python.

## 2. Project Objectives

The main objectives of this project are to:

- Develop a working habit-tracking application using Python.
- Apply object-oriented programming principles through a `Habit` class.
- Store and retrieve data using an SQLite relational database.
- Analyse habit completion history using functions.
- Calculate the longest daily and weekly completion streaks.
- Compare streak durations across habits with different periodicities.
- Apply input validation and exception handling.
- Write unit tests to verify important application behaviours.
- Organise the application into separate modules that are easier to understand, test, and maintain.

## 3. Application Features

### 3.1 Create Habits

Users can create a habit by entering a name and selecting its periodicity.

The application supports two periodicities:

- `daily` — for habits intended to be completed every day.
- `weekly` — for habits intended to be completed every week.

The `Habit` class validates the habit name and periodicity. Empty names and unsupported periodicity values are rejected.

Each habit receives a creation timestamp.

### 3.2 View All Habits

Users can view all habits saved in the database.

The application displays each habit's ID, name, periodicity, and creation timestamp.

### 3.3 Mark Habits as Completed

Users can select a habit by its ID and record a completion.

Each completion is saved with a date and time, creating a history that can be used for later analysis.

The application checks whether the selected habit ID exists before recording the completion.

### 3.4 View Individual Habits

Users can view an individual habit's details, including its name, periodicity, creation timestamp, and completion history.

If a habit has no completion records, the application displays an appropriate message.

### 3.5 Delete Habits

A habit can be deleted by entering its ID.

Associated completion records are also deleted because the SQLite database uses a foreign-key relationship with `ON DELETE CASCADE`.

### 3.6 Filter Habits by Periodicity

Users can view daily habits and weekly habits separately.

This makes it easier to organise and review habits according to their intended frequency.

### 3.7 Analyse Habit Streaks

The application calculates the longest completion streak for daily and weekly habits.

A daily streak represents consecutive calendar days with at least one recorded completion.

A weekly streak represents consecutive ISO calendar weeks with at least one recorded completion.

The application provides two analytics options:

- **Longest streak across all habits:** compares the elapsed calendar-day duration of each habit's longest streak and displays the habit with the greatest duration.
- **Longest streak for one habit:** calculates and displays the longest streak for a selected habit.

The application uses the `longest_streak_duration()` function to compare streak durations across daily and weekly habits.

If a habit has no completion records, its longest streak count is zero. For duration-based comparison, a streak containing only one completion has zero elapsed days.

### 3.8 Load Predefined Sample Data

The application includes five predefined habits for demonstration and testing:

| Habit | Periodicity |
|---|---|
| Read for 20 minutes | Daily |
| Exercise | Weekly |
| Study Python | Daily |
| Drink water | Daily |
| Plan the week | Weekly |

The sample-data module provides example completion records covering four weeks:

- Daily habits can receive 28 sample completion records.
- Weekly habits can receive four sample completion records.

Before creating a predefined habit, the loader checks whether it already exists. It also skips adding sample completion records when the habit already has completion history.

The loader does not automatically fill missing sample records for a habit that already has some completion history.

Sample data helps demonstrate how the application and analytics functions work. It should not be interpreted as actual user activity.

## 4. Technologies Used

### Python

Python is used to implement the application's logic, classes, functions, menu, and input handling.

### SQLite

SQLite provides persistent storage for habits and their completion records. It is accessed through Python's built-in `sqlite3` module.

### Datetime

Python's `datetime` functionality is used to record creation and completion timestamps, identify consecutive completion periods, and calculate streak durations.

### Unittest

Python's built-in `unittest` framework is used to test the Habit class, database operations, and analytics functions.

The current implementation uses Python's standard library and does not require a separate database server.

## 5. Project Structure

The project contains eight Python files and a README documentation file.

| File | Description |
|---|---|
| `main.py` | Contains the command-line menu and coordinates user interaction with the application. |
| `habit.py` | Defines the `Habit` class, validates habit information, records completions in the object, and displays habit details. |
| `database.py` | Defines the `HabitTracker` class and manages SQLite tables and database operations. |
| `analytics.py` | Contains functions for calculating the longest daily and weekly streaks and comparing streak durations in calendar days. |
| `sample_data.py` | Defines predefined habits and generates example completion records. |
| `test_habit.py` | Contains unit tests for the Habit class. |
| `test_database.py` | Contains unit tests for database operations. |
| `test_analytics.py` | Contains unit tests for daily and weekly streak calculations and elapsed streak durations. |
| `README.md` | Documents the project, features, installation, database design, testing, and limitations. |

The application also creates a database file named `habits.db` when it runs with the default database configuration.

## 6. Database Design

The application uses two related SQLite tables: `habits` and `completions`.

### 6.1 Habits Table

The `habits` table stores the main information about each habit.

| Column | Purpose |
|---|---|
| `id` | Unique identifier for each habit. |
| `name` | Name of the habit. |
| `periodicity` | Habit frequency, restricted to `daily` or `weekly`. |
| `created_at` | Date and time when the habit was created. |

The `id` column is the primary key. The periodicity column has a database constraint to prevent unsupported values.

### 6.2 Completions Table

The `completions` table stores the completion history of each habit.

| Column | Purpose |
|---|---|
| `id` | Unique identifier for each completion record. |
| `habit_id` | Foreign key identifying the associated habit. |
| `completed_at` | Date and time when the habit was completed. |

The `habit_id` column references the `id` column in the `habits` table.

Foreign-key enforcement is enabled. The database also uses `ON DELETE CASCADE`, which removes completion records associated with a habit when that habit is deleted.

This database design separates habit information from completion history and allows each habit to have multiple completion records.

## 7. Installation and Setup

### Requirements

- Python 3 installed on the computer.
- The project files saved in the same project folder.
- PyCharm or another Python editor, if preferred.

### Step 1: Open the Project

Open the `habit_tracker_app_!` project folder in PyCharm.

Ensure that PyCharm is configured to use a valid Python interpreter or virtual environment.

### Step 2: Open the Terminal

Open the terminal in PyCharm and navigate to the project folder if necessary.

Check the installed Python version by running:

```bash
python --version
```

If the `python` command is unavailable on Windows, try:

```bash
py --version
```

### Step 3: Run the Application

Run this command inside the project directory:

```bash
python main.py
```

The application should display the main menu.

No separate SQLite installation is required because SQLite support is provided through Python's built-in `sqlite3` module.

## 8. How to Use the Application

When the application starts, it displays the following menu options.

| Option | Function |
|---|---|
| `1` | Create a habit. |
| `2` | View all habits. |
| `3` | Mark a habit as complete. |
| `4` | View one habit and its completion history. |
| `5` | Delete a habit. |
| `6` | View daily habits. |
| `7` | View weekly habits. |
| `8` | View the longest streak across all habits by elapsed calendar duration. |
| `9` | View the longest streak for one habit. |
| `10` | Load predefined sample data. |
| `0` | Exit the application. |

Select an option by entering its number, then follow the prompts.

When creating a habit, enter its name and select either `daily` or `weekly`.

When marking a habit as complete or viewing its details, enter the habit ID shown in the application.

The application validates numeric IDs and checks whether the selected habit exists before performing the requested operation.

The SQLite database retains saved records between application sessions.

## 9. Analytics Implementation

The analytics module contains three main functions:

- `longest_daily_streak(completions)`
- `longest_weekly_streak(completions)`
- `longest_streak_duration(completions, periodicity)`

### 9.1 `longest_daily_streak(completions)`

This function receives a list of completion timestamps.

It converts the timestamps into calendar dates, removes duplicate dates, sorts the dates, and counts consecutive dates.

If a date is missing between two recorded completion dates, the current streak resets.

The function returns the longest daily streak as an integer. It returns `0` when the completion list is empty. A single recorded completion counts as a daily streak of one.

### 9.2 `longest_weekly_streak(completions)`

This function receives a list of completion timestamps.

It converts the timestamps into dates, groups them by ISO calendar year and week, and identifies consecutive weeks.

A gap between calendar weeks resets the current streak.

The function returns the longest weekly streak as an integer. It returns `0` when the completion list is empty. A single recorded completion week counts as a weekly streak of one.

### 9.3 `longest_streak_duration(completions, periodicity)`

This function compares streaks using elapsed calendar days.

For daily habits, it identifies consecutive dates and measures the elapsed days between the beginning and end of each consecutive run.

For weekly habits, it groups completions by ISO calendar week and identifies consecutive weeks. It measures duration from the Monday of the first consecutive week to the Monday of the last consecutive week.

The function returns the elapsed duration of the longest streak in calendar days. It returns `0` when the completion history is empty or when the longest streak contains only one date or week.

The function accepts `daily` or `weekly` as the periodicity. An unsupported periodicity raises a `ValueError`.

### 9.4 Longest Streak Across All Habits

Option 8 retrieves each saved habit and its completion history from the database.

It passes each habit's completion records and periodicity to `longest_streak_duration()`.

The application compares the returned durations and displays the habit with the greatest elapsed calendar-day duration.

If two habits have the same duration, the first habit encountered in the database is displayed.

This approach allows daily and weekly habits to be compared using a common unit of elapsed calendar days rather than directly comparing a number of days with a number of weeks.

### 9.5 Longest Streak for One Habit

Option 9 calculates the longest streak for an individual habit using the relevant daily or weekly streak function.

The result is expressed as a number of consecutive days for a daily habit or consecutive weeks for a weekly habit.

A longest streak is not necessarily the current streak. Historical completion records may contain a longer streak than the one most recently achieved.

## 10. Testing

The project uses Python's `unittest` framework to verify important behaviours.

### 10.1 Habit Tests

**File:** `test_habit.py`

These tests check the behaviour of the `Habit` class, including habit creation, validation, timestamps, and completion history.

**Latest reported result: 10 tests passed.**

### 10.2 Database Tests

**File:** `test_database.py`

These tests check database operations such as adding habits, retrieving saved habits, saving completion records, retrieving completion history, and deleting habits.

They also test that completion records are removed when their associated habit is deleted.

**Latest reported result: 5 tests passed.**

### 10.3 Analytics Tests

**File:** `test_analytics.py`

These tests check daily and weekly streak calculations, including empty histories, individual completions, consecutive completion periods, and elapsed streak durations.

The duration tests include consecutive daily completions, consecutive weekly completions, empty completion histories, and a single completion.

**Latest reported result: 9 tests passed.**

### 10.4 Running the Tests

Run the test files individually from the project folder:

```bash
python -m unittest test_habit.py
```

```bash
python -m unittest test_database.py
```

```bash
python -m unittest test_analytics.py
```

To discover and run all tests automatically, use:

```bash
python -m unittest discover -v
```

The `-v` option displays the names of the tests as they run.

### 10.5 Test Summary

The latest reported individual test runs produced the following results:

| Test file | Tests passed |
|---|---:|
| `test_habit.py` | 10 |
| `test_database.py` | 5 |
| `test_analytics.py` | 9 |
| **Total** | **24** |

All 24 tests passed in the latest reported individual test runs.

The complete test suite should also be run after code changes to check that the tests are discovered and pass together.

## 11. Limitations and Implementation Notes

The current application has the following limitations:

- It uses a command-line interface rather than a graphical or web interface.
- It records completions but does not automatically enforce a habit schedule.
- It does not send reminders or notifications.
- Streak calculations depend on the completion timestamps stored in the database.
- Sample completion records are demonstration data and should not be treated as real activity.
- The sample-data loader skips sample records for a habit that already has completion history. Consequently, a predefined habit with existing manual completions may not receive a full four weeks of sample records.
- When comparing streaks, weekly duration is measured from the Monday of the first consecutive week to the Monday of the last consecutive week, rather than from the first actual completion timestamp to the last actual completion timestamp.
- If multiple habits have the same longest elapsed duration, the first matching habit encountered in the database is displayed.
- The current test suite covers key scenarios, although full coverage of every edge case and input combination is not guaranteed.

A streak represents the longest sequence of consecutive periods with recorded completions. It does not necessarily represent the current streak.

## 12. Possible Future Improvements

Future development could include:

- Adding more tests for invalid inputs and edge cases.
- Improving sample-data loading for habits that already exist.
- Calculating current streaks in addition to longest streaks.
- Displaying completion counts and completion percentages.
- Adding more detailed analytics and habit summaries.
- Improving error messages and input handling.
- Separating additional application logic from the main menu.
- Developing a graphical user interface.
- Adding reminders or scheduled notifications.
- Adding tests for comparing streak durations across multiple habits, including ties and different periodicities.

These improvements could make the application more useful and strengthen its reliability.

## 13. Learning Outcomes

Developing this project provides practical experience with:

- Object-oriented programming and class design.
- Functions, loops, conditionals, and exception handling.
- Input validation and command-line interaction.
- SQLite tables, primary keys, foreign keys, and SQL queries.
- Data persistence between application sessions.
- Date and time handling.
- Daily and weekly streak analysis.
- Comparing durations across different periodicities.
- Unit testing and debugging.
- Modular code organisation and documentation.

## 14. Conclusion

Habit Tracker demonstrates how Python can be used to build a modular command-line application that stores data persistently and analyses habit completion history.

The project combines object-oriented programming, SQLite database management, streak calculations, sample-data generation, and automated testing. The addition of elapsed calendar-duration comparisons makes it possible to compare daily and weekly habit streaks using a common unit of measurement.

Its modular structure also provides a foundation for future improvements, additional analytics, and further development.


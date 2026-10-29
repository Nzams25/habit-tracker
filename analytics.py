
from datetime import datetime


def longest_daily_streak(completions):
    """Calculate the longest sequence of consecutive daily completions."""
    if not completions:
        return 0

    dates = sorted({
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").date()
        for timestamp in completions
    })

    longest_streak = 1
    current_streak = 1

    for index in range(1, len(dates)):
        difference = (dates[index] - dates[index - 1]).days

        if difference == 1:
            current_streak += 1
        else:
            current_streak = 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak


def longest_weekly_streak(completions):
    """Calculate the longest sequence of consecutive weekly completions."""
    if not completions:
        return 0

    dates = sorted({
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").date()
        for timestamp in completions
    })

    weeks = sorted({
        date.isocalendar()[:2]
        for date in dates
    })

    longest_streak = 1
    current_streak = 1

    for index in range(1, len(weeks)):
        previous_week = weeks[index - 1]
        current_week = weeks[index]

        from datetime import date, timedelta

        previous_monday = date.fromisocalendar(
            previous_week[0], previous_week[1], 1
        )
        current_monday = date.fromisocalendar(
            current_week[0], current_week[1], 1
        )

        if (current_monday - previous_monday) == timedelta(days=7):
            current_streak += 1
        else:
            current_streak = 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak



def longest_streak_duration(completions, periodicity):
    """Return the elapsed calendar days in the longest consecutive streak."""
    from datetime import datetime, timedelta

    if not completions:
        return 0

    dates = sorted({
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").date()
        for timestamp in completions
    })

    if periodicity == "daily":
        longest_duration = 0
        current_start = dates[0]
        previous_date = dates[0]

        for current_date in dates[1:]:
            if current_date - previous_date != timedelta(days=1):
                current_start = current_date

            duration = (current_date - current_start).days
            longest_duration = max(longest_duration, duration)
            previous_date = current_date

        return longest_duration

    elif periodicity == "weekly":
        weeks = sorted({
            date.isocalendar()[:2]
            for date in dates
        })

        week_dates = [
            datetime.fromisocalendar(year, week, 1).date()
            for year, week in weeks
        ]

        longest_duration = 0
        current_start = week_dates[0]
        previous_date = week_dates[0]

        for current_date in week_dates[1:]:
            if current_date - previous_date != timedelta(days=7):
                current_start = current_date

            duration = (current_date - current_start).days
            longest_duration = max(longest_duration, duration)
            previous_date = current_date

        return longest_duration

    else:
        raise ValueError("Periodicity must be 'daily' or 'weekly'")










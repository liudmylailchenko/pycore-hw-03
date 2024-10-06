from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        today = datetime.strptime("2024.12.30", "%Y.%m.%d").date()

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= next_week:
            if birthday_this_year.weekday() >= 5:
                congratulation_date = birthday_this_year + timedelta(
                    days=(7 - birthday_this_year.weekday())
                )
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.01"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "test test", "birthday": "1997.01.03"},
]

get_upcoming_birthdays(users)

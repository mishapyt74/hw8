from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    current_date = datetime.now().date()

    start_of_week = current_date - timedelta(days=current_date.weekday())

    birthdays_by_weekday = {i: [] for i in range(7)}

    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=current_date.year).date()

        weekday = (birthday - start_of_week).days % 7

        birthdays_by_weekday[weekday].append(name)

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for weekday_idx, names in birthdays_by_weekday.items():
        if names:
            weekday_name = weekdays[weekday_idx]
            names_str = ", ".join(names)
            print(f"{weekday_name}: {names_str}")

users = [
    {'name': 'Bill', 'birthday': datetime(1993, 2, 5)},
    {'name': 'Jill', 'birthday': datetime(1999, 6, 19)},
    {'name': 'Kim', 'birthday': datetime(2001, 1, 30)},
    {'name': 'Jan', 'birthday': datetime(2005, 3, 29)},

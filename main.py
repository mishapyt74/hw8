from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    current_date = datetime.now()

    start_of_next_week = current_date + timedelta(days=(7 - current_date.weekday()))

    birthdays_by_weekday = {
        0: [],  # Понеділок
        1: [],  # Вівторок
        2: [],  # Середа
        3: [],  # Четвер
        4: [],  # Пятниц
        5: [],  # Субота
        6: []  # Неділя
    }

    for user in users:
        birthday_weekday = user['birthday'].weekday()

        if user['birthday'] >= start_of_next_week:
            birthday_weekday = (birthday_weekday + 7) % 7

        birthdays_by_weekday[birthday_weekday].append(user['name'])

    for weekday, names in birthdays_by_weekday.items():
        if names:
            weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][weekday]
            print(f"{weekday_name}: {', '.join(names)}")

users = [
    {'name': 'Bill', 'birthday': datetime(2023, 2, 5)},
    {'name': 'Jill', 'birthday': datetime(2023, 6, 19)},
    {'name': 'Kim', 'birthday': datetime(2023, 1, 30)},
    {'name': 'Jan', 'birthday': datetime(2023, 3, 29)},
]

get_birthdays_per_week(users)

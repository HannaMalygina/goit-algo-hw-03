# Вимоги до завдання:

# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.

# Рекомендації для виконання:

# Імпортуйте модуль datetime.
# Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
# Отримайте поточну дату, використовуючи datetime.today().
# Розрахуйте різницю між поточною датою та заданою датою.
# Поверніть різницю у днях як ціле число.

# Критерії оцінювання:

# Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
# Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
# Читабельність коду: код повинен бути чистим і добре документованим.
import datetime
from datetime import datetime, timedelta

def get_days_from_today(date_set):
    date_now = datetime.today()
    try:
        date_set_object = datetime.strptime(date_set, "%Y-%m-%d")
        difference = (date_now - date_set_object).days
        return difference

    except ValueError:
        print ("Please enter a date in the following format YYYY-MM-DD")

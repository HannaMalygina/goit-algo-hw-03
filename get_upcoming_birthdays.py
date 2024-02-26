import datetime
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    congratulation_list = []
    today = datetime.today().date()
    this_year = today.year 
    for user in users:
        birthdate = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthdate_this_year = datetime(year = this_year, month = birthdate.month, day = birthdate.day).date()
        congratulation_date = today
        
        if (birthdate_this_year < today-timedelta(days=2)): 
            birthdate_this_year = datetime(year = this_year+1, month = birthdate.month, day = birthdate.day).date()
            congratulation_date = birthdate_this_year
        elif (birthdate_this_year == today-timedelta(days=2) or (birthdate_this_year == today-timedelta(days=1))) and today.weekday() == 0:
            congratulation_date = today
        else:
            if (birthdate_this_year.weekday()==5):
                congratulation_date = birthdate_this_year + timedelta(days=2)
            elif (birthdate_this_year.weekday()==6):
                congratulation_date = birthdate_this_year + timedelta(days=1)
            else:
                congratulation_date = birthdate_this_year
        print(f"{congratulation_date = }")
        if (today + timedelta(days=7) > congratulation_date):
            congratulation_list.append({"name": user["name"], "congratulation_date" : congratulation_date.strftime("%Y.%m.%d")})

    return congratulation_list


users = [
    {"name": "we", "birthday": "1988.01.05"},
    {"name": "th", "birthday": "2010.02.27"},
    {"name": "wn", "birthday": "2012.03.03"},
    {"name": "vb", "birthday": "2014.03.04"},
    {"name": "xc", "birthday": "1988.02.25"},
    {"name": "se", "birthday": "1988.03.02"}
]
print(get_upcoming_birthdays(users))
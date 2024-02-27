import datetime
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    congratulation_list = []
    today = datetime.today().date()
    for user in users:
        birthdate = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthdate_this_year = birthdate.replace(year = today.year)
        congratulation_date = today

        #if birthday already, passed go to the next year 
        if (birthdate_this_year < today-timedelta(days=2)): 
            congratulation_date = birthdate.replace(year = today.year+1)
        #if birthday was last weekend and today is monday
        elif (birthdate_this_year == today-timedelta(days=2) or (birthdate_this_year == today-timedelta(days=1))) and today.weekday() == 0:
            congratulation_date = today
        else:
            if (birthdate_this_year.weekday()==5):
                congratulation_date = birthdate_this_year + timedelta(days=2)
            elif (birthdate_this_year.weekday()==6):
                congratulation_date = birthdate_this_year + timedelta(days=1)
            else:
                congratulation_date = birthdate_this_year
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
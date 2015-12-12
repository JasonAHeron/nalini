import datetime

from nalinixyz.nincal.helpers.calendar_helper import create_month

today = datetime.datetime.date(datetime.datetime.now())

month = create_month(today)
print(month)
for week in month:
    for day in week:
        print(day.day)

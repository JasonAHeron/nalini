import datetime

from nalinixyz.nincal.helpers import create_month

today = datetime.datetime.date(datetime.datetime.now())


print(create_month(today))

import calendar
import datetime
import re


YEAR = ['January',  'February',  'March',  'April',  'May',  'June',  'July',  'August',  'September',  'October',  'November',  'December']


today = datetime.datetime.date(datetime.datetime.now())

month = calendar.monthcalendar(today.year, today.month)





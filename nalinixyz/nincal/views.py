from django.shortcuts import render
import calendar
import datetime


YEAR = ['January',  'February',  'March',  'April',  'May',  'June',  'July',  'August',  'September',  'October',  'November',  'December']


def index(request):
    today = datetime.datetime.date(datetime.datetime.now())
    time_dict = {
        'month_number': today.month,
        'day': today.day,
        'month_name' : YEAR[today.month-1],
        'weeks' : calendar.monthcalendar(today.year, today.month)
    }
    return render(request, 'cal.html', time_dict)

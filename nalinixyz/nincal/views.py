from django.shortcuts import render
import calendar
import datetime
from dateutil.relativedelta import relativedelta


YEAR = ['January',  'February',  'March',  'April',  'May',  'June',  'July',  'August',  'September',  'October',  'November',  'December']


def create_month(previous_month, this_month, next_month):
    last_week_previous_month = previous_month[-1]
    first_week = this_month[0]
    last_week = this_month[-1]
    first_week_next_month = next_month[0]
    fixed_first_week = [previous_month_day or current_month_day for previous_month_day, current_month_day in zip(last_week_previous_month, first_week)]
    fixed_last_week = [current_month_day or next_month_day for current_month_day, next_month_day in zip(last_week, first_week_next_month)]
    return [fixed_first_week] + this_month[1:len(this_month)-1] + [fixed_last_week]


def index(request):
    today = datetime.datetime.date(datetime.datetime.now())
    next = today + relativedelta(months=1)
    previous = today - relativedelta(months=1)
    previous_month = calendar.monthcalendar(previous.year, previous.month)
    this_month = calendar.monthcalendar(today.year, today.month)
    next_month = calendar.monthcalendar(next.year, next.month)

    time_dict = {
        'month_number': today.month,
        'day': today.day,
        'month_name' : YEAR[today.month-1],
        'weeks' : create_month(previous_month, this_month, next_month)
    }
    return render(request, 'cal.html', time_dict)

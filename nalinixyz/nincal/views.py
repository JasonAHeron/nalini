import datetime
from pytz import timezone
from django.shortcuts import render
from nincal.helpers.constants import YEAR
from nincal.helpers.calendar_helper import create_month, get_times
from nincal.helpers.forismatic_api import get_quote
from .models import Day, Poll, Event

def index(request):
    today_in_india = datetime.datetime.now(timezone('Asia/Calcutta'))
    today = today_in_india.date()
    quote, author = get_quote()

    data = {
        'month_number': today.month,
        'day': today.day,
        'month_name' : YEAR[today.month-1],
        'month' : create_month(today),
        'quote': quote,
        'author': author,
        'debug': today_in_india
    }
    return render(request, 'cal.html', data)


def days(request):
    override = request.GET.get('override')

    time_data = get_times(request)
    day = Day.objects.filter(date=time_data['day_iso'])
    if day:
        day = day[0]
        time_data['polls_for_day'] = Poll.objects.filter(day=day)


    if override:
        return render(request, '{}.html'.format(override), time_data)

    if time_data['day_iso'] <= '2015-12-11':
        return render(request, 'withme.html', time_data)

    if time_data['day_iso'] <= time_data['now_iso']:
        return render(request, '{}.html'.format(time_data['day_iso']), time_data)

    else:
        return render(request, 'day_unavailable.html', time_data)

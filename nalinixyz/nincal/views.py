import datetime
from pytz import timezone
from django.shortcuts import render
from .helpers.constants import YEAR
from .helpers.calendar_helper import create_month, get_times
from .helpers.forismatic_api import get_quote
from django.views.decorators.csrf import csrf_exempt
from .polls import polls, update_polls


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


def simple_day(request, time_data):
    return render(request, '{}.html'.format(time_data['day_iso']), time_data)


available_days = {
    '2015-12-12': simple_day,
    '2015-12-13': simple_day,
    '2015-12-14': simple_day,
    '2015-12-15': polls,
    '2015-12-17': simple_day,
}

available_days_post = {
    '2015-12-15': update_polls
}


@csrf_exempt
def days(request):
    day_clicked = request.GET.get('day')
    override = request.GET.get('override')
    time_data = get_times(request)

    if request.POST:
        available_days_post[day_clicked](request, time_data)

    if override:
        day_clicked = override
        return(available_days[day_clicked](request, time_data))

    if time_data['day_iso'] <= '2015-12-11':
        return render(request, 'withme.html', time_data)

    if time_data['day_iso'] <= time_data['now_iso']:
        return(available_days[day_clicked](request, time_data))

    else:
        return render(request, 'day_unavailable.html', time_data)

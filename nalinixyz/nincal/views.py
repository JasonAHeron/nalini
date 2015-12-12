import datetime
from pytz import timezone
from django.shortcuts import render
from nincal.helpers.constants import YEAR
from nincal.helpers.calendar_helper import create_month
from nincal.helpers.forismatic_api import get_quote

def index(request):
    today_in_india = datetime.datetime.now(timezone('Asia/Calcutta'))
    today = today_in_india.date()
    quote, author = get_quote()
    #month = create_month(today)

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
    day_iso = request.GET.get('day')
    now_in_india = datetime.datetime.now(timezone('Asia/Calcutta'))
    now_in_america = datetime.datetime.now(timezone('America/Los_Angeles'))
    now_iso = now_in_india.date().isoformat()
    data = {'day_clicked': day_iso,
            'now_iso': now_iso,
            'time_in_india': now_in_india,
            'time_in_america': now_in_america,
            }

    if day_iso <= '2015-12-11':
        return render(request, 'withme.html', data)
    if day_iso <= now_iso:
        return render(request, '{}.html'.format(day_iso), data)
    else:
        return render(request, 'day_unavailable.html', data)

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
    today_in_india = datetime.datetime.now(timezone('Asia/Calcutta'))
    today_iso = today_in_india.date().isoformat()
    if day_iso <= today_iso:
        return render(request, 'day_1.html', request.GET)
    else:
        return render(request, 'day_unavailable.html')

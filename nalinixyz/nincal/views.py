import datetime
from pytz import timezone
from django.shortcuts import render
from .helpers.constants import YEAR
from .helpers.calendar_helper import create_month
from .helpers.forismatic_api import get_quote


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

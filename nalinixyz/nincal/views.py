import datetime

from django.shortcuts import render
from nincal.helpers.constants import YEAR
from nincal.helpers.calendar_helper import create_month
from nincal.helpers.forismatic_api import get_quote

def index(request):
    today = datetime.datetime.date(datetime.datetime.now())
    quote, author = get_quote()

    data = {
        'month_number': today.month,
        'day': today.day,
        'month_name' : YEAR[today.month-1],
        'month' : create_month(today),
        'quote': quote,
        'author': author
    }
    return render(request, 'cal.html', data)

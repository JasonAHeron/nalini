import datetime
from pytz import timezone
from django.shortcuts import render
from nincal.helpers.constants import YEAR
from nincal.helpers.calendar_helper import create_month, get_times
from nincal.helpers.forismatic_api import get_quote
from django.views.decorators.csrf import csrf_exempt
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

def update_databases(request):
    print(request)
    vote = request.POST.get('vote')
    print(vote)
    if vote:
        p = Poll.objects.get(name=vote)
        p.value += 1
        p.save()


@csrf_exempt
def days(request):
    if request.POST:
        print(request)
        update_databases(request)

    override = request.GET.get('override')

    data = get_times(request)
    day = Day.objects.filter(date=data['day_iso'])
    if day:
        day = day[0]
        data['polls_for_day'] = Poll.objects.filter(day=day)


    if override:
        return render(request, '{}.html'.format(override), data)

    if data['day_iso'] <= '2015-12-11':
        return render(request, 'withme.html', data)

    if data['day_iso'] <= data['now_iso']:
        return render(request, '{}.html'.format(data['day_iso']), data)

    else:
        return render(request, 'day_unavailable.html', data)

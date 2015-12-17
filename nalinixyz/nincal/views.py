import datetime
from pytz import timezone
from django.shortcuts import render
from nincal.helpers.constants import YEAR
from nincal.helpers.calendar_helper import create_month, get_times, get_india_iso
from nincal.helpers.forismatic_api import get_quote
from django.views.decorators.csrf import csrf_exempt
from .models import Day, Poll, Event, Option, Vote


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


def update_polls(request, time_data):
    vote = request.POST.get('vote')
    if vote:
        option = Option.objects.get(name=vote)
        Vote(option=option, time=get_india_iso()).save()



def simple_day(request, time_data):
    return render(request, '{}.html'.format(time_data['day_iso']), time_data)


def polls(request, time_data):
    day = Day.objects.filter(date=time_data['day_iso'])
    if day:
        poll = Poll.objects.get(day=day[0])
        options = Option.objects.filter(poll=poll)
        time_data['poll'] = poll
        time_data['options'] = {option.name: option.value for option in options}
        time_data['votes'] = {option.name: [int(v.time) for v in Vote.objects.filter(option=option)] for option in options}
        all_votes = Vote.objects.all()
        avt = {int(vote.time):vote.name for vote in all_votes}
        time_data['all_vote_times'] = avt
        time_data['all_votes'] = [0] + sorted(list(avt.keys()), reverse=True)
        time_data['Jason'] = [0]
        time_data['Nalini'] = [0]
        for key, value in sorted(avt.items(), key=lambda x:int(x[0])):
            if value == 'Jason':
                time_data['Jason'].append(time_data['Jason'][-1]+1)
                time_data['Nalini'].append(time_data['Nalini'][-1])

            else:
                time_data['Nalini'].append(time_data['Nalini'][-1]+1)
                time_data['Jason'].append(time_data['Jason'][-1])
    return render(request, '2015-12-15.html', time_data)


available_days = {
    '2015-12-12': simple_day,
    '2015-12-13': simple_day,
    '2015-12-14': simple_day,
    '2015-12-15': polls,
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

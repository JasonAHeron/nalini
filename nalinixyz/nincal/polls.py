from .models import Day, Poll, Option, Vote
from .helpers.calendar_helper import get_india_iso
from django.shortcuts import render

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


def update_polls(request, time_data):
    vote = request.POST.get('vote')
    if vote:
        option = Option.objects.get(name=vote)
        Vote(option=option, time=get_india_iso()).save()

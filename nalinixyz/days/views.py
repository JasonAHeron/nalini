from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from nincal.models import Day, Poll, Event, Option, Vote
from nincal.helpers.calendar_helper import create_month, get_times, get_india_iso

def update_databases(request):
    print(request)
    vote = request.POST.get('vote')
    if vote:
        option = Option.objects.get(name=vote)
        Vote(option=option, time=get_india_iso()).save()


@csrf_exempt
def days(request, clicked_day):
    if request.POST:
        print(request)
        update_databases(request)

    override = request.GET.get('override')

    data = get_times(request, clicked_day)
    day = Day.objects.filter(date=data['day_iso'])
    if day:
        poll = Poll.objects.get(day=day[0])
        options = Option.objects.filter(poll=poll)
        data['poll'] = poll
        data['options'] = {option.name: option.value for option in options}
        data['votes'] = {option.name: [int(v.time) for v in Vote.objects.filter(option=option)] for option in options}
        all_votes = Vote.objects.all()
        avt = {int(vote.time):vote.name for vote in all_votes}
        data['all_vote_times'] = avt
        data['all_votes'] = [0] + sorted(list(avt.keys()), reverse=True)
        data['Jason'] = [0]
        data['Nalini'] = [0]
        for key, value in sorted(avt.items(), key=lambda x:int(x[0])):
            if value == 'Jason':
                data['Jason'].append(data['Jason'][-1]+1)
                data['Nalini'].append(data['Nalini'][-1])

            else:
                data['Nalini'].append(data['Nalini'][-1]+1)
                data['Jason'].append(data['Jason'][-1])


    if override:
        return render(request, '{}.html'.format(override), data)

    if data['day_iso'] <= '2015-12-11':
        return render(request, 'withme.html', data)

    if data['day_iso'] <= data['now_iso']:
        return render(request, '{}.html'.format(data['day_iso']), data)

    else:
        return render(request, 'day_unavailable.html', data)

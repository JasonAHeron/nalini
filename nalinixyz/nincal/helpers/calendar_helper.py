import calendar
import datetime
from pytz import timezone

def create_month(today):
    return calendar.Calendar().monthdatescalendar(today.year, today.month)


def get_times(request):
    return {
        'day_iso' : datetime.datetime(*map(int, (request.GET.get('day') or request.GET.get('override')).split('-'))).date().isoformat(),
        'now_in_india' : datetime.datetime.now(timezone('Asia/Calcutta')),
        'now_in_america' : datetime.datetime.now(timezone('America/Los_Angeles')),
        'now_iso' : datetime.datetime.now(timezone('Asia/Calcutta')).date().isoformat()
    }

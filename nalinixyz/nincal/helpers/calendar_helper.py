import calendar
def create_month(today):
    return calendar.Calendar().monthdatescalendar(today.year, today.month)

from django.contrib import admin
from .models import Day, Event, Poll, Option, Vote

# Register your models here.

admin.site.register(Day)
admin.site.register(Event)
admin.site.register(Poll)
admin.site.register(Option)
admin.site.register(Vote)

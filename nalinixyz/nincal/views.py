from django.shortcuts import render
import calendar

def index(request):
    return render(request, 'cal.html')

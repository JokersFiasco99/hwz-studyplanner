from django.shortcuts import render
from .models import Task

def tasks_by_calendar(request, calendar_id):
    tasks = Task.objects.filter(calendar_id=calendar_id)
    return render(request, 'tasks_by_calendar.html', {'tasks': tasks})

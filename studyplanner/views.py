from django.shortcuts import render
from .models import Task, Habit

def tasks_by_calendar(request, calendar_id):
    tasks = Task.objects.filter(calendar_id=calendar_id)
    return render(request, 'tasks_by_calendar.html', {'tasks': tasks})

def habits_by_user(request, user_id):
    habits = Habit.objects.filter(user_id=user_id)
    return render(request, 'habits_by_user.html', {'habits': habits})


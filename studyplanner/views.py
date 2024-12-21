from django.shortcuts import render
from .models import Task, Habit, Goal, Category

def tasks_by_calendar(request, calendar_id):
    tasks = Task.objects.filter(calendar_id=calendar_id)
    return render(request, 'tasks_by_calendar.html', {'tasks': tasks})

def habits_by_user(request, user_id):
    habits = Habit.objects.filter(user_id=user_id)
    return render(request, 'habits_by_user.html', {'habits': habits})

def goals_by_user(request, user_id):
    goals = Goal.objects.filter(user_id=user_id)
    return render(request, 'goals_by_user.html', {'goals': goals})

def categories_by_task(request, task_id):
    categories = Category.objects.filter(task_id=task_id)
    return render(request, 'categories_by_task.html', {'categories': categories})

def categories_by_habit(request, habit_id):
    categories = Category.objects.filter(habit_id=habit_id)
    return render(request, 'categories_by_habit.html', {'categories': categories})


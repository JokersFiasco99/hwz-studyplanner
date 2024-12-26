from django.shortcuts import render, redirect, get_object_or_404
from .models import Calendar, Category, Task, Habit, StudySession, Goal, Subject
from .forms import CalendarForm, TaskForm, HabitForm, GoalForm, StudySessionForm
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta

def calendar_list(request):
    # Get or create a single calendar for user
    calendar, created = Calendar.objects.get_or_create(
        user_id=1,
        defaults={'name': 'Mein Kalender', 'beschreibung': 'Mein persönlicher Kalender'}
    )
    return redirect('calendar_detail', pk=calendar.id)

def calendar_create(request):
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.user_id = 1
            calendar.save()
            return redirect('calendar_list')
    else:
        form = CalendarForm()
    return render(request, 'calendar_form.html', {'form': form})

def task_list(request):
    sort_by = request.GET.get('sort', 'datum')
    direction = request.GET.get('direction', 'asc')
    
    if sort_by == 'subject':
        order_by = f"{'-' if direction == 'desc' else ''}subject__name"
    else:
        order_by = f"{'-' if direction == 'desc' else ''}{sort_by}"
    
    tasks = Task.objects.filter(user=request.user).order_by(order_by)
    
    return render(request, 'task_list.html', {
        'tasks': tasks,
        'current_sort': sort_by,
        'current_direction': direction
    })

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            calendar = Calendar.objects.filter(user=request.user).first()
            task.kalender = calendar
            task.save()
            
            if task.repeat != 'none':
                if task.repeat == 'daily':
                    days = 1
                elif task.repeat == 'weekly':
                    days = 7
                elif task.repeat == 'biweekly':
                    days = 14
                
                next_date = task.datum + timedelta(days=days)
                Task.objects.create(
                    title=task.title,
                    beschreibung=task.beschreibung,
                    datum=next_date,
                    kalender=calendar,
                    kategorie=task.kategorie,
                    user=task.user,
                    repeat=task.repeat,
                    priority=task.priority,
                    subject=task.subject
                )
            return redirect('task_list')
    else:
        form = TaskForm(user=request.user)
    return render(request, 'task_form.html', {'form': form})

def habit_list(request):
    habits = Habit.objects.filter(user_id=1)
    return render(request, 'habit_list.html', {'habits': habits})

def habit_create(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user_id = 1
            habit.save()
            return redirect('habit_list')
    else:
        form = HabitForm()
    return render(request, 'habit_form.html', {'form': form})

def goal_list(request):
    goals = Goal.objects.filter(user_id=1)
    return render(request, 'goal_list.html', {'goals': goals})

def goal_create(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user_id = 1
            goal.save()
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'goal_form.html', {'form': form})

def study_session_list(request):
    sessions = StudySession.objects.filter(user_id=1)
    return render(request, 'study_session_list.html', {'sessions': sessions})

def study_session_create(request):
    if request.method == "POST":
        form = StudySessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user_id = 1
            session.save()
            return redirect('study_session_list')
    else:
        form = StudySessionForm()
    return render(request, 'study_session_form.html', {'form': form})

def calendar_delete(request, pk):
    calendar = get_object_or_404(Calendar, pk=pk)
    calendar.delete()
    return redirect('calendar_list')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            if task.status == 'erledigt' and task.repeat == 'weekly':
                Task.objects.create(
                    title=task.title,
                    beschreibung=task.beschreibung,
                    datum=task.datum + timedelta(days=7),
                    kalender=task.kalender,
                    kategorie=task.kategorie,
                    user=task.user,
                    repeat=task.repeat
                )
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def habit_update(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save()
            return redirect('habit_list')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habit_form.html', {'form': form})

def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('habit_list')

def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            goal = form.save()
            return redirect('goal_list')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'goal_form.html', {'form': form})

def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.delete()
    return redirect('goal_list')

def calendar_update(request, pk):
    calendar = get_object_or_404(Calendar, pk=pk)
    if request.method == "POST":
        form = CalendarForm(request.POST, instance=calendar)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.user_id = 1
            calendar.save()
            return redirect('calendar_list')
    else:
        form = CalendarForm(instance=calendar)
    return render(request, 'calendar_form.html', {'form': form})

def subject_list(request):
    subjects = Subject.objects.filter(user=request.user)
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Subject.objects.create(name=name, user=request.user)
        return redirect('subject_list')
    return render(request, 'subject_list.html', {'subjects': subjects})

def calendar_detail(request, pk):
    calendar = get_object_or_404(Calendar, pk=pk)
    tasks = Task.objects.filter(kalender=calendar, user=request.user)
    study_sessions = StudySession.objects.filter(kalender=calendar, user=request.user)
    
    return render(request, 'calendar_detail.html', {
        'calendar': calendar,
        'tasks': tasks,
        'study_sessions': study_sessions
    })

def index(request):
    Category.create_defaults()
    if request.user.is_authenticated:
        Calendar.objects.get_or_create(
            user=request.user,
            defaults={
                'name': 'Mein Kalender',
                'beschreibung': 'Mein persönlicher Kalender'
            }
        )
    return render(request, 'index.html')

def subject_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        beschreibung = request.POST.get('beschreibung')
        Subject.objects.create(
            name=name,
            beschreibung=beschreibung,
            user=request.user
        )
        return redirect('task_list')
    return render(request, 'subject_form.html')



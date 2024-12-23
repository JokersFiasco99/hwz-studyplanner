from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Calendar, Task, Habit, Goal, StudySession, Timeslot, Exam

# Calendar Views

class CalendarCreateView(CreateView):
    model = Calendar
    fields = ['name', 'description']
    template_name = 'calendar_form.html'
    success_url = reverse_lazy('calendar_list')

    def form_valid(self, form):
        form.instance.user_id = 1
        return super().form_valid(form)

class CalendarListView(ListView):
    model = Calendar
    template_name = 'calendar_list.html'

    def get_queryset(self):
        return Calendar.objects.filter(user_id=1)

class CalendarDetailView(DetailView):
    model = Calendar
    template_name = 'calendar_detail.html'

class CalendarUpdateView(UpdateView):
    model = Calendar
    fields = ['name', 'description']
    template_name = 'calendar_form.html'
    success_url = reverse_lazy('calendar_list')
class CalendarDeleteView(DeleteView):
    model = Calendar
    template_name = 'calendar_confirm_delete.html'
    success_url = reverse_lazy('calendar_list')

# Task Views

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'calendar', 'category']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    user_id = 1
    context_object_name = 'task_list'

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status', 'calendar', 'category']
    template_name = 'task_form.html'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

# Habit Views

class HabitCreateView(CreateView):
    model = Habit
    fields = ['name', 'status', 'progress', 'target_value', 'category']
    template_name = 'habit_form.html'
    success_url = reverse_lazy('habit_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HabitListView(ListView):
    model = Habit
    template_name = 'habit_list.html'
    user_id = 1
    context_object_name = 'habit_list'

class HabitUpdateView(UpdateView):
    model = Habit
    fields = ['name', 'status', 'progress', 'target_value', 'category']
    template_name = 'habit_form.html'
    success_url = reverse_lazy('habit_list')

class HabitDeleteView(DeleteView):
    model = Habit
    template_name = 'habit_confirm_delete.html'
    success_url = reverse_lazy('habit_list')

# Goal Views

class GoalCreateView(CreateView):
    model = Goal
    fields = ['name', 'description', 'target_value', 'status', 'habit', 'category']
    template_name = 'goal_form.html'
    success_url = reverse_lazy('goal_list')
    user_id = 1

class GoalListView(ListView):
    model = Goal
    template_name = 'goal_list.html'
    user_id = 1
    context_object_name = 'goal_list'

class GoalUpdateView(UpdateView):
    model = Goal
    fields = ['name', 'description', 'target_value', 'status', 'habit', 'category']
    template_name = 'goal_form.html'
    success_url = reverse_lazy('goal_list')

class GoalDeleteView(DeleteView):
    model = Goal
    template_name = 'goal_confirm_delete.html'
    success_url = reverse_lazy('goal_list')

# Study Session Views

class StudySessionCreateView(CreateView):
    model = StudySession
    fields = ['title', 'description', 'start_time', 'end_time', 'calendar', 'status', 'goal']
    template_name = 'study_session_form.html'
    user_id = 1
    success_url = reverse_lazy('study_session_list')

class StudySessionListView(ListView):
    model = StudySession
    template_name = 'study_session_list.html'
    user_id = 1
    context_object_name = 'study_session_list'

class StudySessionUpdateView(UpdateView):
    model = StudySession
    fields = ['title', 'description', 'start_time', 'end_time', 'calendar', 'status', 'goal']
    template_name = 'study_session_form.html'
    success_url = reverse_lazy('study_session_list')

class StudySessionDeleteView(DeleteView):
    model = StudySession
    template_name = 'study_session_confirm_delete.html'
    success_url = reverse_lazy('study_session_list')

# Timeslot Views

class TimeslotCreateView(CreateView):
    model = Timeslot
    fields = ['title', 'start_time', 'end_time', 'study_session']
    template_name = 'timeslot_form.html'
    success_url = reverse_lazy('timeslot_list')

class TimeslotListView(ListView):
    model = Timeslot
    template_name = 'timeslot_list.html'
    user_id = 1
    context_object_name = 'timeslot_list'

class TimeslotUpdateView(UpdateView):
    model = Timeslot
    fields = ['title', 'start_time', 'end_time', 'study_session']
    template_name = 'timeslot_form.html'
    success_url = reverse_lazy('timeslot_list')

class TimeslotDeleteView(DeleteView):
    model = Timeslot
    template_name = 'timeslot_confirm_delete.html'
    success_url = reverse_lazy('timeslot_list')

# Exam Views

class ExamCreateView(CreateView):
    model = Exam
    fields = ['title', 'description', 'date', 'time', 'time_slot']
    template_name = 'exam_form.html'
    success_url = reverse_lazy('exam_list')

class ExamListView(ListView):
    model = Exam
    template_name = 'exam_list.html'
    user_id = 1
    context_object_name = 'exam_list'

class ExamUpdateView(UpdateView):
    model = Exam
    fields = ['title', 'description', 'date', 'time', 'time_slot']
    template_name = 'exam_form.html'
    success_url = reverse_lazy('exam_list')

class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'exam_confirm_delete.html'
    success_url = reverse_lazy('exam_list')



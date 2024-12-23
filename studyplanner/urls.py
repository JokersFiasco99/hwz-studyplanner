"""
URL configuration for studyplanner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/create/', views.CalendarCreateView.as_view(), name='calendar_create'),
    path('calendar/', views.CalendarListView.as_view(), name='calendar_list'),
    path('calendar/<int:pk>/', views.CalendarDetailView.as_view(), name='calendar_detail'),
    path('calendar/<int:pk>/update/', views.CalendarUpdateView.as_view(), name='calendar_update'),
    path('calendar/<int:pk>/delete/', views.CalendarDeleteView.as_view(), name='calendar_delete'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('habit/create/', views.HabitCreateView.as_view(), name='habit_create'),
    path('habits/', views.HabitListView.as_view(), name='habit_list'),
    path('habit/<int:pk>/update/', views.HabitUpdateView.as_view(), name='habit_update'),
    path('habit/<int:pk>/delete/', views.HabitDeleteView.as_view(), name='habit_delete'),
    path('goal/create/', views.GoalCreateView.as_view(), name='goal_create'),
    path('goals/', views.GoalListView.as_view(), name='goal_list'),
    path('goal/<int:pk>/update/', views.GoalUpdateView.as_view(), name='goal_update'),
    path('goal/<int:pk>/delete/', views.GoalDeleteView.as_view(), name='goal_delete'),
    path('study_session/create/', views.StudySessionCreateView.as_view(), name='study_session_create'),
    path('study_sessions/', views.StudySessionListView.as_view(), name='study_session_list'),
    path('study_session/<int:pk>/update/', views.StudySessionUpdateView.as_view(), name='study_session_update'),
    path('study_session/<int:pk>/delete/', views.StudySessionDeleteView.as_view(), name='study_session_delete'),
    path('timeslot/create/', views.TimeslotCreateView.as_view(), name='timeslot_create'),
    path('timeslots/', views.TimeslotListView.as_view(), name='timeslot_list'),
    path('timeslot/<int:pk>/update/', views.TimeslotUpdateView.as_view(), name='timeslot_update'),
    path('timeslot/<int:pk>/delete/', views.TimeslotDeleteView.as_view(), name='timeslot_delete'),
    path('exam/create/', views.ExamCreateView.as_view(), name='exam_create'),
    path('exams/', views.ExamListView.as_view(), name='exam_list'),
    path('exam/<int:pk>/update/', views.ExamUpdateView.as_view(), name='exam_update'),
    path('exam/<int:pk>/delete/', views.ExamDeleteView.as_view(), name='exam_delete'),
]


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
    path('', views.index, name='index'),
    
    # Kalender URLs
    path('calendar/', views.calendar_list, name='calendar_list'),
    path('calendar/<int:pk>/', views.calendar_detail, name='calendar_detail'),
    
    # Aufgaben URLs
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    
    # Habit URLs
    path('habits/', views.habit_list, name='habit_list'),
    path('habits/create/', views.habit_create, name='habit_create'),
    path('habits/<int:pk>/update/', views.habit_update, name='habit_update'),
    path('habits/<int:pk>/delete/', views.habit_delete, name='habit_delete'),
    
    # Study Session URLs
    path('study-sessions/', views.study_session_list, name='study_session_list'),
    path('study-sessions/create/', views.study_session_create, name='study_session_create'),
    
    # Subject URLs
    path('subject/create/', views.subject_create, name='subject_create'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
]


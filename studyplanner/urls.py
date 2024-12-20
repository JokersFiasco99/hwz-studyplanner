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
    path('calendar/<int:calendar_id>/tasks/', views.tasks_by_calendar, name='tasks_by_calendar'),
    path('user/<int:user_id>/habits/', views.habits_by_user, name='habits_by_user'),
    path('user/<int:user_id>/goals/', views.goals_by_user, name='goals_by_user'),
    path('user/categories/', views.categories_by_user, name='categories_by_user'),
]


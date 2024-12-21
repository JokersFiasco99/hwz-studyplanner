from django.contrib import admin
from .models import Calendar, Task, Habit, Goal, Category, Notification, StudySession, Timeslot, Exam

admin.site.register(Calendar)
admin.site.register(Task)
admin.site.register(Habit)
admin.site.register(Goal)
admin.site.register(Category)
admin.site.register(Notification)
admin.site.register(StudySession)
admin.site.register(Timeslot)
admin.site.register(Exam)
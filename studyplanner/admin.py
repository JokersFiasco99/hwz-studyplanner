from django.contrib import admin
from .models import Calendar, Task, Habit, Goal    

admin.site.register(Calendar)
admin.site.register(Task)
admin.site.register(Habit)
admin.site.register(Goal)
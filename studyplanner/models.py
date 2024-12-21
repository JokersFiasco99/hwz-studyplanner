from django.contrib.auth.models import User
from django.db import models

class Calendar(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('STUDIUM', 'Studium'),
        ('ARBEIT', 'Arbeit'),
        ('SPORT', 'Sport'),
        ('FAMILIE', 'Familie'),
        ('FREIZEIT', 'Freizeit'),
    ]

    CATEGORY_DESCRIPTIONS = {
        'STUDIUM': 'Kategorien für Vorlesungen, Prüfungen oder Studienprojekte.',
        'ARBEIT': 'Kategorien für berufliche Termine, Meetings oder Aufgaben.',
        'SPORT': 'Kategorien für Fitness- oder Trainingsaktivitäten.',
        'FAMILIE': 'Kategorien für private Termine oder Familienzeit.',
        'FREIZEIT': 'Kategorien für Hobbys, Ausflüge oder entspannte Aktivitäten.',
    }
    
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def get_description(self):
        return self.CATEGORY_DESCRIPTIONS.get(self.name, 'Keine Beschreibung verfügbar')


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=[('offen', 'Offen'), ('in_arbeit', 'In Arbeit'), ('erledigt', 'Erledigt')], default='offen')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Habit(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    progress = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_value = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Goal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    target_value = models.IntegerField(default=0)
    current_value = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.OneToOneField(Habit, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


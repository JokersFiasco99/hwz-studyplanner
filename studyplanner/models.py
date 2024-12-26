from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Calendar(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True, null=True)
    datum = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=False)

    @classmethod
    def create_defaults(cls):
        defaults = ['Studium', 'Arbeit', 'Sport', 'Familie', 'Freizeit']
        for name in defaults:
            cls.objects.get_or_create(name=name, is_default=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    REPEAT_CHOICES = [
        ('none', 'Keine Wiederholung'),
        ('daily', 'Täglich'),
        ('weekly', 'Wöchentlich'),
        ('biweekly', 'Alle zwei Wochen'),
    ]
    
    PRIORITY_CHOICES = [
        ('niedrig', 'Niedrig'),
        ('mittel', 'Mittel'),
        ('hoch', 'Hoch'),
    ]
    
    title = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True, null=True)
    datum = models.DateField()
    status = models.CharField(max_length=20, default='offen')
    kalender = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    kategorie = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repeat = models.CharField(max_length=10, choices=REPEAT_CHOICES, default='none')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='niedrig')
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Habit(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True, null=True)
    zielwert = models.IntegerField(default=0)
    fortschritt = models.IntegerField(default=0)
    kategorie = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudySession(models.Model):
    title = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True, null=True)
    start_zeit = models.DateTimeField()
    end_zeit = models.DateTimeField()
    kalender = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Notification(models.Model):
    title = models.CharField(max_length=100)
    nachricht = models.TextField()
    datum = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Goal(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True, null=True)
    zielwert = models.IntegerField(default=0)
    fortschritt = models.IntegerField(default=0)
    kategorie = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
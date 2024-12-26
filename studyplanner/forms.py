from django import forms
from .models import Calendar, Task, Habit, Goal, StudySession, Category, Subject

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['name', 'beschreibung', 'datum']
        widgets = {
            'datum': forms.DateInput(attrs={'type': 'date'})
        }

class TaskForm(forms.ModelForm):
    kategorie = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label=None,
        label='Kategorie'
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.none(),
        required=False,
        label='Fach'
    )
    
    class Meta:
        model = Task
        fields = ['title', 'beschreibung', 'datum', 'kategorie', 'priority', 'subject', 'repeat']
        widgets = {
            'datum': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['kategorie'].queryset = Category.objects.all()
        if user:
            self.fields['subject'].queryset = Subject.objects.filter(user=user)

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'beschreibung', 'zielwert', 'fortschritt', 'kategorie']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'beschreibung', 'zielwert', 'fortschritt', 'kategorie']

class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['title', 'beschreibung', 'start_zeit', 'end_zeit', 'kalender']
        widgets = {
            'start_zeit': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_zeit': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        } 
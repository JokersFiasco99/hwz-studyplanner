from django.test import TestCase
from django.contrib.auth.models import User
from .models import Calendar, Task, Habit, Goal, StudySession, Timeslot, Exam
from django.urls import reverse

class CalendarModelTest(TestCase):

    #unit tests
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_calendar_creation(self):
        calendar = Calendar.objects.create(name='Test Calendar', description='This is a test calendar', user=self.user)
        self.assertEqual(calendar.name, 'Test Calendar')
        self.assertEqual(calendar.description, 'This is a test calendar')
        self.assertEqual(calendar.user, self.user)

    def test_calendar_deletion(self):
        calendar = Calendar.objects.create(name='Test Calendar', description='This is a test calendar', user=self.user)
        calendar.delete()
        self.assertEqual(Calendar.objects.count(), 0)

    def test_calendar_not_blank(self):
        calendar = Calendar.objects.create(name='Test Calendar', description='This is a test calendar', user=self.user)
        self.assertNotEqual(calendar.name, '')
        self.assertNotEqual(calendar.description, '')
        self.assertNotEqual(calendar.user, None)

    def test_calendar_no_description(self):
        calendar = Calendar.objects.create(name='Test Calendar', user=self.user)
        self.assertEqual(calendar.description, None)

class CalendarIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.calendar = Calendar.objects.create(name='Test Calendar', description='This is a test calendar', user=self.user)

    def test_calendar_create_view(self):
        response = self.client.post(reverse('calendar_create'), {'name': 'Test Calendar', 'description': 'This is a test calendar'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Calendar.objects.filter(name='Test Calendar').exists())
    
    def test_calendar_list_view(self):
        response = self.client.get(reverse('calendar_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Calendar')

    def test_calendar_detail_view(self):
        response = self.client.get(reverse('calendar_detail', args=[self.calendar.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Calendar')
        self.assertContains(response, 'This is a test calendar')
    
    def test_calendar_update_view(self):
        response = self.client.post(reverse('calendar_update', args=[self.calendar.id]), {'name': 'Updated Calendar', 'description': 'This is an updated calendar'})
        self.assertEqual(response.status_code, 302)
        self.calendar.refresh_from_db()
        self.assertEqual(self.calendar.name, 'Updated Calendar')
        self.assertEqual(self.calendar.description, 'This is an updated calendar')

    def test_calendar_delete_view(self):
        response = self.client.post(reverse('calendar_delete', args=[self.calendar.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Calendar.objects.filter(id=self.calendar.id).exists())


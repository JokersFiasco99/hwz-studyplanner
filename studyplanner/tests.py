from django.test import TestCase
from django.contrib.auth.models import User
from .models import Calendar, Task, Habit, Goal, StudySession, Timeslot, Exam, Category
from django.urls import reverse

class CalendarModelTest(TestCase):

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

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.calendar = Calendar.objects.create(name="Test Calendar", description="Testbeschreibung", user=self.user)
        self.category = Category.objects.create(name="STUDIUM")

    def test_task_creation(self):
        task = Task.objects.create(
            title="Test Task",
            user=self.user,
            calendar=self.calendar,
            category=self.category
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.calendar, self.calendar)
        self.assertEqual(task.category, self.category)

class TaskIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.calendar = Calendar.objects.create(name="Test Calendar", description="Beschreibung", user=self.user)
        self.category = Category.objects.create(name="STUDIUM")
        self.task = Task.objects.create(
            title="Test Task",
            user=self.user,
            calendar=self.calendar,
            category=self.category
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_create_view(self):
        response = self.client.post(
            reverse('task_create'),
            data={
                'title': 'Neuer Task',
                'description': 'Test Description',
                'deadline': '',
                'status': 'offen',
                'calendar': self.calendar.id,
                'category': self.category.id
            }
        )
        print(response.context['form'].errors if response.context else "No form errors")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='Neuer Task').exists())

class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name="STUDIUM")

    def test_habit_creation(self):
        habit = Habit.objects.create(
            name="Test Habit",
            user=self.user,
            target_value=10,
            category=self.category
        )
        self.assertEqual(habit.name, "Test Habit")
        self.assertEqual(habit.user, self.user)
        self.assertEqual(habit.target_value, 10)
        self.assertEqual(habit.category, self.category)

class HabitIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.category = Category.objects.create(name="STUDIUM")
        self.habit = Habit.objects.create(
            name="Test Habit",
            user=self.user,
            target_value=10,
            category=self.category
        )

    def test_habit_list_view(self):
        response = self.client.get(reverse('habit_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Habit")

    def test_habit_create_view(self):
        response = self.client.post(
            reverse('habit_create'),
            data={
                'name': 'Neuer Habit',
                'status': False,
                'progress': 0,
                'target_value': 5,
                'category': self.category.id
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Habit.objects.filter(name='Neuer Habit').exists())

    def test_habit_update_view(self):
        response = self.client.post(
            reverse('habit_update', args=[self.habit.id]),
            data={
                'name': 'Updated Habit',
                'status': True,
                'progress': 5,
                'target_value': 15,
                'category': self.category.id
            }
        )
        self.assertEqual(response.status_code, 302)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.name, 'Updated Habit')
        self.assertEqual(self.habit.target_value, 15)
        self.assertEqual(self.habit.progress, 5)
        self.assertTrue(self.habit.status)

    def test_habit_delete_view(self):
        response = self.client.post(reverse('habit_delete', args=[self.habit.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())

class GoalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name="STUDIUM")
        self.habit = Habit.objects.create(
            name="Test Habit", 
            user=self.user, 
            target_value=10, 
            category=self.category
        )

    def test_goal_creation(self):
        goal = Goal.objects.create(
            name="Test Goal",
            target_value=100,
            current_value=50,
            habit=self.habit,
            user=self.user,
            category=self.category
        )
        self.assertEqual(goal.name, "Test Goal")
        self.assertEqual(goal.target_value, 100)
        self.assertEqual(goal.current_value, 50)

class GoalIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.category = Category.objects.create(name="STUDIUM")
        self.habit = Habit.objects.create(
            name="Test Habit", 
            user=self.user, 
            target_value=10, 
            category=self.category
        )

    def test_goal_list_view(self):
        response = self.client.get(reverse('goal_list'))
        self.assertEqual(response.status_code, 200)

    def test_goal_create_view(self):
        response = self.client.post(
            reverse('goal_create'),
            data={
                'name': 'New Goal',
                'target_value': 100,
                'current_value': 0,
                'habit': self.habit.id,
                'category': self.category.id
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Goal.objects.filter(name='New Goal').exists())

class StudySessionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.calendar = Calendar.objects.create(name="Test Calendar", description="Test Description", user=self.user)
        self.category = Category.objects.create(name="STUDIUM")
        self.habit = Habit.objects.create(name="Test Habit", user=self.user, target_value=10, category=self.category)
        self.goal = Goal.objects.create(
            name="Test Goal",
            target_value=100,
            current_value=50,
            habit=self.habit,
            user=self.user,
            category=self.category
        )

    def test_study_session_creation(self):
        study_session = StudySession.objects.create(
            title="Test Session",
            start_time="2024-01-01 09:00:00",
            end_time="2024-01-01 10:00:00",
            calendar=self.calendar,
            user=self.user
        )
        self.assertEqual(study_session.title, "Test Session")
        self.assertEqual(study_session.calendar, self.calendar)
        self.assertEqual(study_session.user, self.user)

class StudySessionIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.calendar = Calendar.objects.create(name="Test Calendar", description="Test Description", user=self.user)
        self.category = Category.objects.create(name="STUDIUM")
        self.habit = Habit.objects.create(name="Test Habit", user=self.user, target_value=10, category=self.category)
        self.goal = Goal.objects.create(
            name="Test Goal",
            target_value=100,
            current_value=50,
            habit=self.habit,
            user=self.user,
            category=self.category
        )

    def test_study_session_list_view(self):
        response = self.client.get(reverse('study_session_list'))
        self.assertEqual(response.status_code, 200)

    def test_study_session_create_view(self):
        response = self.client.post(
            reverse('study_session_create'),
            data={
                'title': 'New Session',
                'start_time': '2024-01-01 09:00:00',
                'end_time': '2024-01-01 10:00:00',
                'calendar': self.calendar.id,
                'status': 'geplant'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(StudySession.objects.filter(title='New Session').exists())

class TimeslotModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.calendar = Calendar.objects.create(name="Test Calendar", description="Test Description", user=self.user)
        self.study_session = StudySession.objects.create(
            title="Test Session",
            start_time="2024-01-01 09:00:00",
            end_time="2024-01-01 10:00:00",
            calendar=self.calendar,
            user=self.user
        )

    def test_timeslot_creation(self):
        timeslot = Timeslot.objects.create(
            title="Test Timeslot",
            start_time="2024-01-01 09:00:00",
            end_time="2024-01-01 10:00:00",
            study_session=self.study_session,
            user=self.user
        )
        self.assertEqual(timeslot.title, "Test Timeslot")
        self.assertEqual(timeslot.study_session, self.study_session)
        self.assertEqual(timeslot.user, self.user)

class TimeslotIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.calendar = Calendar.objects.create(name="Test Calendar", description="Test Description", user=self.user)
        self.study_session = StudySession.objects.create(
            title="Test Session",
            start_time="2024-01-01 09:00:00",
            end_time="2024-01-01 10:00:00",
            calendar=self.calendar,
            user=self.user
        )
        self.timeslot = Timeslot.objects.create(
            title="Test Timeslot",
            start_time="2024-01-01 09:00:00",
            end_time="2024-01-01 10:00:00",
            study_session=self.study_session,
            user=self.user
        )

    def test_timeslot_list_view(self):
        response = self.client.get(reverse('timeslot_list'))
        self.assertEqual(response.status_code, 200)

    def test_timeslot_create_view(self):
        response = self.client.post(
            reverse('timeslot_create'),
            data={
                'title': 'New Timeslot',
                'start_time': '2024-01-01 14:00:00',
                'end_time': '2024-01-01 15:00:00',
                'study_session': self.study_session.id
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Timeslot.objects.filter(title='New Timeslot').exists())

class ExamModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.calendar = Calendar.objects.create(name="Test Calendar", description="Test Description", user=self.user)
        self.study_session = StudySession.objects.create(
            title="Test Session",
            start_time="2024-01-01 09:00:00",
            end_time="2024-01-01 10:00:00",
            calendar=self.calendar,
            user=self.user
        )
        self.timeslot = Timeslot.objects.create(
            title="Test Timeslot",
            start_time="2024-01-01 09:00:00",
            end_time="2024-01-01 10:00:00",
            study_session=self.study_session,
            user=self.user
        )

    def test_exam_creation(self):
        exam = Exam.objects.create(
            title="Test Exam",
            description="Test Description",
            date="2024-01-01",
            time="09:00",
            user=self.user,
            time_slot=self.timeslot
        )
        self.assertEqual(exam.title, "Test Exam")
        self.assertEqual(exam.description, "Test Description")
        self.assertEqual(exam.user, self.user)
        self.assertEqual(exam.time_slot, self.timeslot)

class ExamIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.calendar = Calendar.objects.create(name="Test Calendar", description="Test Description", user=self.user)
        self.study_session = StudySession.objects.create(
            title="Test Session",
            start_time="2024-01-01 09:00:00",
            end_time="2024-01-01 10:00:00",
            calendar=self.calendar,
            user=self.user
        )
        self.timeslot = Timeslot.objects.create(
            title="Test Timeslot",
            start_time="2024-01-01 09:00:00",
            end_time="2024-01-01 10:00:00",
            study_session=self.study_session,
            user=self.user
        )

    def test_exam_list_view(self):
        response = self.client.get(reverse('exam_list'))
        self.assertEqual(response.status_code, 200)

    def test_exam_create_view(self):
        response = self.client.post(
            reverse('exam_create'),
            data={
                'title': 'New Exam',
                'description': 'Test Description',
                'date': '2024-01-01',
                'time': '09:00',
                'time_slot': self.timeslot.id
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Exam.objects.filter(title='New Exam').exists())


from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Note, Task


class ProductiveTodoAppTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username='alice',
            email='alice@example.com',
            password='StrongPassword123',
        )
        self.other_user = self.User.objects.create_user(
            username='bob',
            email='bob@example.com',
            password='StrongPassword123',
        )
        self.client.login(username='alice', password='StrongPassword123')

    def test_user_can_create_task(self):
        response = self.client.post(
            reverse('task_create'),
            {
                'title': 'Rédiger le rapport',
                'description': 'Version finale',
                'due_date': '2026-10-20T09:00',
                'completed': False,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(user=self.user, title='Rédiger le rapport').exists())

    def test_dashboard_shows_only_user_tasks(self):
        Task.objects.create(user=self.user, title='Tâche utilisateur', completed=True)
        Task.objects.create(user=self.other_user, title='Tâche autre user', completed=False)

        response = self.client.get(reverse('dashboard'))

        self.assertContains(response, 'Tâche utilisateur')
        self.assertNotContains(response, 'Tâche autre user')

    def test_user_can_create_note(self):
        response = self.client.post(
            reverse('note_create'),
            {'title': 'Idée produit', 'content': 'Créer une version bêta'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(user=self.user, title='Idée produit').exists())

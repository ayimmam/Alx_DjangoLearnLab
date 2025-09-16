from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

class RoleBasedAccessTest(TestCase):
    def setUp(self):
        # Create users with different roles
        self.admin_user = User.objects.create_user(username='admin', password='password')
        UserProfile.objects.filter(user=self.admin_user).update(role='Admin')

        self.librarian_user = User.objects.create_user(username='librarian', password='password')
        UserProfile.objects.filter(user=self.librarian_user).update(role='Librarian')

        self.member_user = User.objects.create_user(username='member', password='password')
        # The default role is 'Member', so no update is needed

        self.client = Client()

    def test_admin_view_access(self):
        # Test access for Admin user
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationship_app/admin_view.html')

    def test_admin_view_rejection(self):
        # Test access for non-Admin users
        for username in ['librarian', 'member']:
            self.client.login(username=username, password='password')
            response = self.client.get(reverse('admin_view'))
            self.assertNotEqual(response.status_code, 200)

        # Test access for anonymous user
        self.client.logout()
        response = self.client.get(reverse('admin_view'))
        self.assertNotEqual(response.status_code, 200)
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        # Client simulates a browser and the creation of a user
        # which GET and POST requests can be made from.
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@test.com',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='raymond@test.com',
            password='test123',
            name='test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on the users page"""

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # This send a GET to the URL defined above and
        # expects a response status of 200.
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

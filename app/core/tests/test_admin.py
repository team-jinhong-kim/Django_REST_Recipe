from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@jakekim.com',
            password='testjake123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@jakekim.com',
            password='testjake123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""

        # These urls are listed in django admin docs
        # Gets the URL that lists users in admin page
        # have to register User model to admin for this url to work
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # check if response contain new user name and email
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

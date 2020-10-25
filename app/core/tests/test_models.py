from django.test import TestCase
from django.contrib.auth get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test Creating a new user with an email is successful"""
        email = 'test@jakekim.com'
        password = 'testjake123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

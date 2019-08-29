from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        '''Test creating a new user with email is successful'''
        email = 'ajay.b@servify.in'
        password = 'ajay1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test that email for a new user is normalized'''
        email = 'ajay.b@SERVIFY.IN'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test creating user with no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        '''Test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'ajay.b@servify.in',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

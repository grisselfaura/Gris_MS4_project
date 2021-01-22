from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import UserProfile, create_or_update_user_profile
import json
# from django.contrib.auth.models import User, AnonymousUser
# from django.shortcuts import get_object_or_404
# from accounts.views import register, login, logout, profile


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_profile_page_GET(self):
        """
        Tests that the login page view renders the login template
        """
        response = self.client.get(reverse('profile'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

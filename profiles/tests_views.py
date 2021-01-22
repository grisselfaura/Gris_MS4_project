from django.test import TestCase, RequestFactory
from profiles.models import UserProfile
from django.shortcuts import get_object_or_404
from profiles.views import profile, order_history


# class TestProfilesViews(TestCase):

#     def test_get_profile_page(self):
        # """
        # Tests that the user can view the profile page when user is logged in
        # """
        # self.client.login(username='userprofileName', password='userprofilePassword')
        # response = self.client.get('/profiles/profile/')
        # self.assertEqual(response.status_code, 200)

    # def test_get_order_history_page(self):
    #     """
    #     Tests that the login page view renders the login template
    #     """
    #     response = self.client.get('/checkout/checkout_success/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'checkout/checkout_success.html')

    # def setUp(self):
    #     self.client = Client()

    # def test_profile_page_GET(self):
    #     """
    #     Tests that the login page view renders the login template
    #     """
    #     response = self.client.get(reverse('profile'))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'profiles/profile.html')

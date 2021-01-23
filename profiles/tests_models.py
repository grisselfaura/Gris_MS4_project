# from django.test import TestCase, RequestFactory
# from profiles.models import UserProfile

# class TestProfilesModels(TestCase):

#     def setUp(self):
#         self.client = Client()

#     def test_profile_page_GET(self):
#         """
#         Tests that the login page view renders the login template
#         """
#         response = self.client.get(reverse('profile'))

#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'profiles/profile.html')

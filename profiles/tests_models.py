from django.test import TestCase, RequestFactory
from .models import UserProfile


class TestProfilesModels(TestCase):

    # def setUp(self):
    #     self.client = Client()

    # def test_profile_page_GET(self):
    #     """
    #     Tests that the login page view renders the login template
    #     """
    #     response = self.client.get(reverse('profile'))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_default(self):
        profile = UserProfile(default_full_name='Test Billing Name',
                              default_street_address1='Test Address1',
                              default_street_address2='Test Address2',
                              default_town_or_city='Test City',
                              default_postcode='Test Postcode',
                              default_country='Test Country')

        self.assertEqual(profile.default_full_name, 'Test Billing Name')
        self.assertEqual(profile.default_street_address1, 'Test Address1')
        self.assertEqual(profile.default_street_address2, 'Test Address2')
        self.assertEqual(profile.default_town_or_city, 'Test City')
        self.assertEqual(profile.default_postcode, 'Test Postcode')
        self.assertEqual(profile.default_country, 'Test Country')

    # def test_request_fullname(self):
    #     profile = UserProfile(default_full_name='Test New User Name')
    #     profile.save()
    #     self.assertEqual(profile.default_full_name, 'Test New User Name')

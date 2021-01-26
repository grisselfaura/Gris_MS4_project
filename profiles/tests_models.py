from django.test import TestCase
from .models import UserProfile


class TestProfilesModels(TestCase):

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

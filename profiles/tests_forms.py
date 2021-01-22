from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForms(TestCase):

    def test_create_profile_form_with_required_fields_filled(self):
        form = UserProfileForm({
            'full_name': 'Carlos Ramos',
            'email': 'cramos@gmail.com',
            'phone_number': '+31 123456 789',
            'address_line1': '123 test street',
            'town_or_city': 'test city',
            'country': 'NL'})
        self.assertTrue(form.is_valid())

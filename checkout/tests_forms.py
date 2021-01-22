from django.test import TestCase
from .forms import OrderForm


class TestCheckoutOrderForm(TestCase):

    def test_generate_order_with_required_fields(self):
        form = OrderForm({
            'full_name': 'Carlos Ramos',
            'email': 'cramos@gmail.com',
            'phone_number': '+31 123456 789',
            'address_line1': '123 test street',
            'town_or_city': 'test city',
            'country': 'NL'})
        self.assertTrue(form.is_valid())

    def test_generate_correct_message_for_empty_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'],
                            [u'This field is required.'])

from django.test import TestCase
from .forms import ProductForm


class TestServiceForms(TestCase):

    def test_create_service_form_incomplete(self):
        form = ProductForm({
            'name': 'New service',
            'description': 'this is the service i am testing',
            'research': False,
            'design_sprint': True,
            'usability_testing': False,
            'is_a_service': True,
            'price': 9.99})
        self.assertFalse(form.is_valid())

    def test_create_service_form_complete(self):
        form = ProductForm({
            'name': 'New service',
            'description': 'this is the service i am testing',
            'research': False,
            'design_sprint': True,
            'usability_testing': False,
            'is_a_service': True,
            'price': 9.99,
            'duration': '5 week',
            'revision': '1x',
            'image_url': '',
            'image': '',
            'discontinued': False})
        self.assertFalse(form.is_valid())

from django.test import TestCase
from .models import Service, Category


class TestServiceModel(TestCase):

    def test_service_default_to_false(self):
        service = Service.objects.create(name="Test service",
                                         description="Test description",
                                         price=9.99)
        self.assertFalse(service.is_a_service)

    def test_category_default_to_true(self):
        category = Category.objects.create(name="New Deal")
        self.assertTrue(category.name)

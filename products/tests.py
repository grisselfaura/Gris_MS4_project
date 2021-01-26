from django.test import TestCase
from .models import Service


class TestModel(TestCase):

    def test_done_default_to_false(self):
        product = Service.objects.create(name="Test Service",
                                         description="Service description",
                                         price=499)
        self.assertFalse(product.is_a_service)

from django.test import TestCase
from products.models import Service, Category


class TestBagViews(TestCase):

    def test_view_bag(self):
        categories = Category(name="Category Name")
        categories.save()
        service_detail = Service(name="Test service", price=999.00,
                                 description="Test service description",
                                 image="test.jpg")
        service_detail.save()
        response = self.client.get("/bag/")
        self.assertEqual(response.status_code, 200)

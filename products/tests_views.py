from django.test import TestCase
from .models import Service, Category


class TestServiceViews(TestCase):
    def test_get_services_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/services.html')

    def test_get_service_details_page(self):
        categories = Category(name="Category Name")
        categories.save()
        service_detail = Service(name="Test service", price=999.00,
                                 description="Test service description",
                                 image="test.jpg")
        service_detail.save()

        response = self.client.get("/products/1/")
        self.assertEqual(response.status_code, 200)

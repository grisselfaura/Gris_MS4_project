from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import all_services, add_product, \
 service_detail, edit_product, delete_product


class TestServiceUrls(SimpleTestCase):

    def test_all_services_url_resolves(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, all_services)

    def test_add_url_resolves(self):
        url = reverse('add_product')
        self.assertEquals(resolve(url).func, add_product)

    def test_service_detail_url_resolves(self):
        url = reverse('service_detail', args=('1',))
        self.assertEquals(resolve(url).func, service_detail)

    # def test_edit_url_resolves(self):
    #     url = reverse('edit_product', args=int('service'))
    #     self.assertEquals(resolve(url).func, edit_product)

    # def test_delete_url_resolves(self):
    #     url = reverse('delete_product', args=int('service'))
    #     self.assertEquals(resolve(url).func, delete_product)
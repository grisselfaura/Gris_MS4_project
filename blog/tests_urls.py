from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import blog


class TestUrls(SimpleTestCase):

    def test_blog_url_resolves(self):
        url = reverse('urban_blog')
        self.assertEquals(resolve(url).func, blog)

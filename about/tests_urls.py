from django.test import SimpleTestCase
from django.urls import reverse, resolve
from about.views import about, portfolio, connect, portfolio_detail


class TestUrls(SimpleTestCase):

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_portfolio_url_resolves(self):
        url = reverse('my_portafolio')
        self.assertEquals(resolve(url).func, portfolio)

    def test_connect_url_resolves(self):
        url = reverse('lets_connect')
        self.assertEquals(resolve(url).func, connect)

    # def test_portfolio_detail_url_resolves(self):
    #     url = reverse('my_portfolio_slider', args=[portfolio])
    #     self.assertEquals(resolve(url).func, portfolio_detail)

    # def test_portfolio_detail_url_resolves(self):
    #     url = reverse('my_portfolio_slider', args=int('portfolio'))
    #     self.assertEquals(resolve(url).func, portfolio_detail)

    # def test_portfolio_detail_url_resolves(self):
    #     url = reverse('my_portfolio_slider', args=[int(portfolio)])
    #     self.assertEquals(resolve(url).func, portfolio_detail)

    # def test_portfolio_detail_url_resolves(self):
    #     url = reverse('my_portfolio_slider', args=['some-portfolio'])
    #     self.assertEquals(resolve(url).func, portfolio_detail)

#path('<int:portfolio_id>/', views.portfolio_detail, name='my_portfolio_slider')
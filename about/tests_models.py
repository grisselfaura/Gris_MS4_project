from django.test import TestCase
from .models import Portfolio


class TestPotfolioModel(TestCase):

    def test_portfolio_default_to_false(self):
        portfolios = Portfolio.objects.create(name='portfolio work', likes=10,
                                              views=99, image_cover='',
                                              image_slide_1='')
        self.assertFalse(portfolios.name)

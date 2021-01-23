from django.test import TestCase
from .models import Portfolio


class TestPotfolioModel(TestCase):

    def test_portfolio_default_to_false(self):
        portfolios = Portfolio.objects.create(name="portfolio example work",
                                              likes=10, views=99,
                                              image_cover="cover_img_1.jpg",
                                              image_slide_1="slide_img_1.jpg")
        self.assertEqual(portfolios.name, "portfolio example work")
        self.assertEqual(portfolios.image_slide_1, "slide_img_1.jpg")
        self.assertTrue(portfolios.likes)
        self.assertTrue(portfolios.views)
        self.assertFalse(portfolios.name_client)

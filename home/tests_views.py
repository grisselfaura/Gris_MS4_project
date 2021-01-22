from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/includes/back_to_top.html")
        self.assertTemplateUsed(response, "home/includes/home_education.html")
        self.assertTemplateUsed(response, "home/includes/home_experience.html")
        self.assertTemplateUsed(response,
                                "home/includes/home_landing_img.html")
        self.assertTemplateUsed(response, "home/includes/home_reviews.html")

from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=254)
    name_client = models.CharField(max_length=254)
    likes = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) #not used in the database(testing adding to field at a later stage)
    views = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) #not used in the database(testing adding to field at a later stage)
    image_url_cover = models.URLField(max_length=1024, null=True, blank=True)
    image_url_slide_1 = models.URLField(max_length=1024, null=True, blank=True)
    image_url_slide_2 = models.URLField(max_length=1024, null=True, blank=True)
    image_url_slide_3 = models.URLField(max_length=1024, null=True, blank=True)
    image_url_slide_4 = models.URLField(max_length=1024, null=True, blank=True)
    image_url_slide_5 = models.URLField(max_length=1024, null=True, blank=True)
    image_url_slide_6 = models.URLField(max_length=1024, null=True, blank=True)
    image_url_slide_7 = models.URLField(max_length=1024, null=True, blank=True)
    image_url_slide_8 = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_name_client(self):
        return self.name_client

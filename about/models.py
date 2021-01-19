from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=254)
    name_client = models.CharField(max_length=254)
    likes = models.DecimalField(max_digits=6,
                                decimal_places=0, null=True, blank=True)
    views = models.DecimalField(max_digits=6,
                                decimal_places=0, null=True, blank=True)
    image_cover = models.ImageField(null=True, blank=True)
    image_slide_1 = models.ImageField(null=True, blank=True)
    image_slide_2 = models.ImageField(null=True, blank=True)
    image_slide_3 = models.ImageField(null=True, blank=True)
    image_slide_4 = models.ImageField(null=True, blank=True)
    image_slide_5 = models.ImageField(null=True, blank=True)
    image_slide_6 = models.ImageField(null=True, blank=True)
    image_slide_7 = models.ImageField(null=True, blank=True)
    image_slide_8 = models.ImageField(null=True, blank=True)
    image_slide_9 = models.ImageField(null=True, blank=True)
    image_slide_10 = models.ImageField(null=True, blank=True)
    image_slide_11 = models.ImageField(null=True, blank=True)
    image_slide_12 = models.ImageField(null=True, blank=True)
    image_slide_13 = models.ImageField(null=True, blank=True)
    image_slide_14 = models.ImageField(null=True, blank=True)
    image_slide_15 = models.ImageField(null=True, blank=True)
    image_slide_16 = models.ImageField(null=True, blank=True)
    image_slide_17 = models.ImageField(null=True, blank=True)
    image_slide_18 = models.ImageField(null=True, blank=True)
    image_slide_19 = models.ImageField(null=True, blank=True)
    image_slide_20 = models.ImageField(null=True, blank=True)
    image_slide_21 = models.ImageField(null=True, blank=True)
    image_slide_22 = models.ImageField(null=True, blank=True)
    image_slide_23 = models.ImageField(null=True, blank=True)
    image_slide_24 = models.ImageField(null=True, blank=True)
    image_slide_25 = models.ImageField(null=True, blank=True)
    image_slide_26 = models.ImageField(null=True, blank=True)
    image_slide_27 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_name_client(self):
        return self.name_client

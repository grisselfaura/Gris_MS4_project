from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Service(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    research = models.BooleanField(default=True)
    design_sprint = models.BooleanField(default=False)
    usability_testing = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_a_service = models.BooleanField(default=False)
    duration = models.TextField()
    revision = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    discontinued = models.BooleanField(default=False)

    def __str__(self):
        return self.name

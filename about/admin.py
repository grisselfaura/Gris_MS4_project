from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'name_client',
        'likes',
        'views',
        'image_cover',
    )


admin.site.register(Portfolio, PortfolioAdmin)

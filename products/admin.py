from django.contrib import admin
from .models import Service, Category


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'research',
        'design_sprint',
        'usability_testing',
        'price',
        'is_a_service',
        'duration',
        'revision',
        'image',
        'discontinued',
    )

    ordering = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)

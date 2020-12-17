from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_services, name='products'),
    path('<int:service_id>/', views.service_detail, name='service_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:service_id>/', views.edit_product, name='edit_product'),
]

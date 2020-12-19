from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('portafolio/', views.portafolio, name='my_portafolio'),
    path('connect/', views.connect, name='lets_connect'),
]
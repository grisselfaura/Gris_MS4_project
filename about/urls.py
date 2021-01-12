from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('portafolio/', views.portfolio, name='my_portafolio'),
    path('portfolio_test/', views.portfolio_test, name='portfolio_test'),
    path('connect/', views.connect, name='lets_connect'),
    path('testportfoliodetalio/', views.portfolio_detail, name='portfolio_slide_example')
]

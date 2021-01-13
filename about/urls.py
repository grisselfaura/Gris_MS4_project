from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('portfolio/', views.portfolio, name='my_portafolio'),
    # path('portfolio_test/', views.old_portfolio, name='portfolio_test'),
    path('connect/', views.connect, name='lets_connect'),
    path('testportfoliodetalio/', views.portfolio_detail, name='portfolio_slide_example')
]

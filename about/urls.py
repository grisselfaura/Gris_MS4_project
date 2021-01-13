from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('portfolio/', views.portfolio, name='my_portafolio'),
    # path('portfolio_test/', views.old_portfolio, name='portfolio_test'),
    path('connect/', views.connect, name='lets_connect'),
    # path('portfolio_slider/', views.portfolio_detail, name='my_portfolio_slider'),
    path('<int:portfolio_id>/', views.portfolio_detail, name='my_portfolio_slider')
]

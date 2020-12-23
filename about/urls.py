from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('portafolio/', views.portfolio, name='my_portafolio'),
    path('connect/', views.connect, name='lets_connect'),
    path('testportfoliodetalio/', views.portfolio_detail, name='portfolio_slide_example'),
    # path('<int:portafolio_id>/', views.portfolio_detail, name='portfolio_slide_example'),
]


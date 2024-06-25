from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Start'),
    path('kalkulator', views.calculator, name='Kalkulator'),
    path('informacje', views.news, name='Infromacje'),
    path('ceny', views.prices, name='Ceny'),
    path('pogoda', views.weather, name='Pogoda'),
    path('mapy', views.maps, name='Mapy')
]

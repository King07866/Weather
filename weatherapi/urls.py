from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('weather/', views.home, name="home"),
    path('weatherapi/', views.ForecastWeather, name="index")
]
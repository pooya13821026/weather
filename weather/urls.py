from django.urls import path
from weather import views

urlpatterns = [
    path('', views.WeatherDetail.as_view())
]

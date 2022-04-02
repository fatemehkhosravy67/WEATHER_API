from django.urls import path
from . import views
urlpatterns = [
    path('weather-api/<city>', views.get_weather),
    ]
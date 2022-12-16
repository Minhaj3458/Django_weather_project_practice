from django.urls import path
app_name = 'App_weather'
from .import views
urlpatterns = [
   path('', views.CityWeatherView, name="CityWeatherView"),
   path('remove/<city_name>/',views.City_delete, name='city_remove')
]
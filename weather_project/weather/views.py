import requests
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import City
from django.core.cache import cache
import json


@api_view(['GET'])
def get_weather(request, city):
    # reading from cache
    city_in_cache = cache.get(city)
    if city_in_cache is not None:
        print('this data is in cache')
        return Response(json.loads(city_in_cache), status=status.HTTP_200_OK)
    # reading from db
    city_in_db = City.objects.filter(name=city).first()
    if city_in_db is not None:
        rtn = dict(name=city_in_db.name, icon=city_in_db.icon, temperature=city_in_db.temperature,
                   description=city_in_db.description)
        cache.set(city, json.dumps(rtn))
        return Response(rtn, status=status.HTTP_200_OK)
    # reading from API
    print('this data is new')
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f4149d0d859828b86a82f7fdb6c0fc14"
    response = requests.get(url.format(city)).json()
    rtn = {
        'city': city.upper(),
        'icon': response['weather'][0]['icon'],
        'temperature': int(response['main']['temp']),
        'description': response['weather'][0]['description'],
    }
    cache.set(city, json.dumps(rtn))
    City(name=rtn['city'], icon=rtn['icon'], temperature=rtn['temperature'],
         description=rtn['description']).save()
    return Response(rtn, status=status.HTTP_200_OK)

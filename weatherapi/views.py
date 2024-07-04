import requests
import json
import urllib.request
import datetime as dts
from datetime import datetime
from django.utils.timezone import timedelta
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'first_page.html')

def ForecastWeather(request):
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = 'ebd5e2636f15368a8d026e0dfe4b1fb6'

        base_url = 'http://api.openweathermap.org/data/2.5/forecast'

        params = {
            'q': city,
            'appid': api_key,
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        # Extract relevant information from the API response
        forecasts = []
        for entry in data['list']:
            forecast = {
                "Day" : dts.datetime.fromtimestamp(entry['dt']).strftime("%A"),
                "Temp" : int(entry['main']['temp'] - 273.15, ),
                "Description" : entry['weather'][0]['description'],
                "Icon" : entry['weather'][0]['icon'],
            }
            forecasts.append(forecast)

        return render(request, 'weather_app.html', {'forecast' : forecasts, 'city' : city})


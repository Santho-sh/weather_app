from django.shortcuts import render
import requests

# Create your views here.
def index(response):
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=4d17d5e441962a4f45bdefd41ce3208d'
    
    location = 'Las Vegas'
    
    data = requests.get(url.format(location)).json()
    print(data)
    
    weather = {
        'city': location,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }
    
    print(weather)
    
    return render(response, 'weather/index.html')
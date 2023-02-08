from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(response):
    
    # you need to get your own api key and paste it in below url
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={API KEY}'
    
    if response.method == 'POST':
        form = CityForm(response.POST)
        form.save()
    
    form = CityForm()
    
    cities = City.objects.all()
    weather_data = []
    
    for city in cities:
    
        data = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        weather_data.append(weather)
    
    return render(response, 'weather/index.html', {'weather_data':weather_data, 'form': form})
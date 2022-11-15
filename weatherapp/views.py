from django.shortcuts import render
import requests
from django.http import HttpResponse
import json
from pprint import pprint as pp
# Create your views here.


def index(request):
    context = {}
    if request.method == 'POST':
        
        location = request.POST['location']
        data = ''
        json_data = None
        try:
            data = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ location +'&appid=845fbddc53f11264927270674491d34d').json()
            context =  {
            
            "city": data['name'],
            "lat" : int(data['coord']['lat']),
            "long": int(data['coord']['lon']),
            "wind_speed": data['wind']['speed'],
            "deg": int(data['main']['temp'] ) - 273,
            "humidity": data['main']['humidity'],

        }
        except requests.ConnectionError:
            return HttpResponse('<h2>An error occured while getting the data.</h2> <br><br>Please check your internet connection and try again.')
        
        
        pp(json_data)

        
    return render(request, "index.html", context)


def news(request):
    return render(request, "news.html")


def cameras(request):
    return render(request, "live-cameras.html")


def photos(request):
    return render(request, "photos.html")


def contact(request):
    return render(request, "contact.html")


def single(request):
    return render(request, "single.html")

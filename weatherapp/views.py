from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, Http404
import json
from pprint import pprint as pp
from django.views import View
from django.views.generic import ListView
from .process_image import get_image
# Create your views here.


def index(request):
    context = {}
    weather_data = []
    
    if request.method == 'POST':
        
        location = request.POST['location']
        request.session['location'] = location
        
        data = ''
        json_data = None
        images = []
        try:
            data = requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+ location +'&cnt=40&appid=845fbddc53f11264927270674491d34d').json()
            #pp(data)
            
            for i in range(1, len(data['list']), 8):
                weather_data.append(data['list'][i])
                images.append(get_image(data['list'][i]['weather'][0]['id']))
            
            context =  {
            "weather_details": weather_data,
            "code": data['city']['country'],
            "city": data['city']['name'],
            "lat" : int(data['city']['coord']['lat']),
            "long": int(data['city']['coord']['lon']),
            "image": images
            }
            
        except requests.ConnectionError:
            raise ConnectionError
        except KeyError:
            return redirect('/')

    return render(request, "index.html", context)


class PhotoListView(ListView):
    
    def get(self, request, *args, **kwargs):
        a = []
        mylocation = request.session.get('location')
        photorequest = requests.get('https://pixabay.com/api/?key=31754217-1e506785a2df45438b2ff9a60&q='+ str(mylocation)).json()

        data = []
        try:
            for i in range(10):
                data.append(photorequest['hits'][i])    
        except IndexError:
            return redirect('/')


        try:
            del request.session['location']
        except KeyError:
            return redirect('/')
        except NameError:
            return redirect('/')
        return render(request, 'photos.html', {'data': data})

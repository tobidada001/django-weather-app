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

    return render(request, "index.html", context)

class IndexView(View):
    template_name = "index.html"
    context = {}
    weather_data = []
    data = ''
    json_data = None
    images = []
   
    def get(self, request, *args, **kwargs):
        context = request.session.get('context')
        
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        location = request.POST['location']
        weather_data = []
        images = []
        request.session['location'] = location

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
            request.session['context'] = context
            
        except requests.ConnectionError:
            return redirect('index')
        except KeyError:
            return redirect('/')

        return redirect(request.path)
        

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

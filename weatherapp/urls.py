from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('news', views.news, name = 'news'),
    path('live-cameras', views.cameras, name = 'live_cameras'),
    path('photos', views.photos, name = 'photos'),
    path('contact', views.contact, name = 'contact'),
]

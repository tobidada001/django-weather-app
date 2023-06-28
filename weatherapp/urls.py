from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('photos', views.PhotoListView.as_view(), name = 'photos'),
    path('test/', views.index, name='test')
]

from django.url import path  
from .import views

ulrpatterns = [
    path('', views.inicio, name='inicio')
]

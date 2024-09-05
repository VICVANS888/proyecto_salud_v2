from django.urls import path
from . import views

urlpatterns = [
    path('intro/', views.intro_interface, name='intro_interface'),
]

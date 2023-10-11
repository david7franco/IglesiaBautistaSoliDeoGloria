from django.urls import path
from . import views 
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('contact/', views.contact, name='contacto'),
    path('donate/', views.donation, name='donation'),
    path('process_donation/', views.process_donation, name='process_donation'),
    path('sermons/', views.sermons, name='Predicaciones'),
    path('about_us/', views.about_us, name='about_us'),
    path('toggle_letter/', views.toggle_letter, name='toggle_letter'),
    path('thank_you/', views.thank_you, name='thank_you_page'),
]

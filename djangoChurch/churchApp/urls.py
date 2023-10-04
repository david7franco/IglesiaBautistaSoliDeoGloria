from django.urls import path
from . import views 
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('contact/', views.contact, name='contacto'),
    path('donate/', views.donation, name='donation'),
    path('process_donation/', views.process_donation, name='process_donation'),
    path('about_us/', views.about_us, name='Acerca De Nosotros'),
]

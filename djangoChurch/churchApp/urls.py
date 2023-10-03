from django.urls import path
from . import views 
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('', views.contact, name='contact'),
]

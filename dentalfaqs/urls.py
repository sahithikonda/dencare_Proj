from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='DentalFAQs-home'),
    path('services', views.services, name='services'),
    path('prices', views.Prices, name='Prices'),
    path('Contact', views.Contact, name='Contact'),
    path('getback', views.getback, name='getback')
]


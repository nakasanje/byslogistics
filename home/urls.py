from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('track_request/', views.track_request, name='track_request'),

     path('contact/', views.contact_view, name='contact'),
     path('services/delivery', views.services_delivery, name='services_delivery'),
     path('services/storage/', views.storage_service, name='storage_service'),
path('services/business-support/', views.business_support, name='business_support'),
     path('about/values/', views.about_values, name='about_values'),
    path('about/technology/', views.about_technology, name='about_technology'),
    path('about/academy/', views.about_academy, name='about_academy'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
   
]

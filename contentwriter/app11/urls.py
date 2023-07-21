from django.urls import path
from app11 import views

urlpatterns = [
    path('', views.ContentPage),
    path('contactDetails/', views.ContactDetails),
    path('register_login/', views.RegisterLogin),
    path('register/', views.register_request),
]
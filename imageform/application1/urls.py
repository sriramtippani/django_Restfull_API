from django.urls import path
from application1 import views

urlpatterns = [
    path('', views.homeView),
    path('page2/', views.formView),
    path('page3/', views.lastView),
]
from django.urls import path
from testapplication1.api import views

urlpatterns = [
    path('lc/', views.ApiListCreateView.as_view()),
    path('rud/<int:pk>', views.ApiUpdateRetriveDestroyView.as_view()),
]
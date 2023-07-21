from django.urls import path
from application1.api import views

from rest_framework_simplejwt.views import (
         TokenObtainPairView,
         TokenRefreshView,
)

urlpatterns = [
    path('a1/', views.HotelListCreate.as_view()),
    path('a2/<int:pk>', views.HotelRetrieveUpdateDestroy.as_view()),
    path('api11/', TokenObtainPairView.as_view()),
    path('api22/', TokenRefreshView.as_view()),
]

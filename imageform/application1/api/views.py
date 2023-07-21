from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from application1.models import Hotel
from application1.api.serializers import HotelSerializer
from rest_framework.permissions import IsAuthenticated


class HotelListCreate(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated, ]


class HotelRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated, ]
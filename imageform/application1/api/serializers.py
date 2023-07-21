from rest_framework.serializers import ModelSerializer
from application1.models import Hotel

class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
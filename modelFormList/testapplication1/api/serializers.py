from rest_framework import serializers
from testapplication1.models import modelForm1
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = modelForm1
        fields = '__all__'
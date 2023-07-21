from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from testapplication1.models import modelForm1
from testapplication1.api.serializers import FormSerializer

class ApiListCreateView(ListCreateAPIView):
    queryset = modelForm1.objects.all()
    serializer_class = FormSerializer

class ApiUpdateRetriveDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = modelForm1.objects.all()
    serializer_class = FormSerializer
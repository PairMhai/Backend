from membership.models import Customer, Class
from membership.serializers import CustomerSerializer, ClassSerializer
# from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics

#Create your views here.
class CustomerAction(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        print("self: " + str(self.request))
        print("serializer: " + str(serializer))
        serializer.save(self.request.user)

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ClassDetail(generics.RetrieveAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    # example of custom response json format
    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response({"successful" : True, "data": serializer.data})

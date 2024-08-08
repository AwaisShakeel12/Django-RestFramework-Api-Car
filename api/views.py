from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from rest_framework import mixins, generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token


users = User.objects.all()

for user in users:
    token = Token.objects.get_or_create(user=user)



# Create your views here.

class OnlyAdmin(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        if request.method== 'GET':
            return True
        if request.method == 'POST' or request.FILES or request.method == "PUT" or request.method == "DELETE":
            if user.is_superuser:
                return True
        
        return False
  


class BrandListView(generics.ListCreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class VehicleTypeListView(generics.ListCreateAPIView):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [ OnlyAdmin]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        wrapped_response = {"vehicles": serializer.data}
        return Response(wrapped_response)


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class VehicleTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer



from django.urls import path
from api.views import BrandListView, VehicleTypeListView, VehicleListView,VehicleDetailView, BrandDetailView, VehicleTypeDetailView
from rest_framework.authtoken.views import obtain_auth_token

# jwt-----------------

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
   path('', VehicleListView.as_view(), name='vehicle-list'),
   path('brand/', BrandListView.as_view(), name='brand-list'),
   path('type/', VehicleTypeListView.as_view(), name='type-list'),
   path('<int:pk>/', VehicleDetailView.as_view(), name='type-list'),
   path('brand/<int:pk>/', BrandDetailView.as_view(), name='type-list'),
   path('type/<int:pk>/', VehicleTypeDetailView.as_view(), name='type-list'),
   path('login/' ,obtain_auth_token, name='login'),


   # ----------jwt----------------------------
   path('login/jwt/', TokenObtainPairView.as_view(), name='create-token'),
   path('login/refresh/', TokenRefreshView.as_view(), name='refresh-token'),


]
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    phone_number = models.BigIntegerField(null=True , blank=True)
   
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username



class VehicleType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Brand(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name



class Vehicle(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='vehicle_images' , null=True, blank=True, default='images/avatar.jpg' )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    
    def __str__(self):
        return self.title

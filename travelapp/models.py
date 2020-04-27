from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=200)
    bestlink = models.CharField(max_length=200)
    weekgetlinks = models.CharField(max_length=200)

    def __str__(self):
        return self.city


class Flights(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    flight_num = models.CharField(max_length=10)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    eprice = models.IntegerField(null=True)
    dept_time = models.TimeField(auto_now=False,auto_now_add=False)
    dest_time = models.TimeField(auto_now=False,auto_now_add=False)
    company = models.CharField(max_length=15,default=" ")
    seats = models.IntegerField()


    def __str__(self):
        return self.flight_num

class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=200)
    hotel_address = models.CharField(max_length=500)
    hotel_price = models.IntegerField(null=True)
    hotel_rating = models.IntegerField(null=True)
    amenities = models.CharField(max_length=500)
    distfromap = models.IntegerField(null=True)
    rooms = models.IntegerField(default=0)
    image1 = models.ImageField(null=True,upload_to='img/')


    def __str__(self):
        return self.hotel_name

class Famous(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    place_name = models.CharField(max_length=200)
    image = models.ImageField(null=True,upload_to='img/')
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.place_name

class BookFlight(models.Model):
    username_id = models.ForeignKey(User,on_delete=models.CASCADE)
    flight = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    seat = models.IntegerField(default=1)

    def __str__(self):
        return self.date

class BookHotel(models.Model):
    username_id = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    room = models.IntegerField(default=1)

    def __str__(self):
        return self.date

class BookPackage(models.Model):
    username_id = models.ForeignKey(User,on_delete=models.CASCADE)
    seat = models.IntegerField(default=1)
    flight = models.CharField(max_length=10)
    hotel_name = models.CharField(max_length=10)
    room = models.IntegerField(default=1)
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.date

from django.db import models

# Create your models here.

class Bus_list(models.Model):
    name = models.CharField(max_length=100)
    form = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    
    
    def __str__(self):
        return self.name

class Shedule(models.Model):
    class Status_type(models.TextChoices):
        ON_TRIP = "TRIP", "On a trip"
        NOT_ON_TRIP = "NO", "Not on a trip"
        
    bus = models.ForeignKey(Bus_list, on_delete=models.CASCADE)
    time = models.TimeField()
    am = models.BooleanField()
    pm = models.BooleanField()
    status = models.CharField(max_length=10, choices=Status_type.choices)

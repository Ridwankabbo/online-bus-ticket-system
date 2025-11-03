from django.db import models

# Create your models here.

class Locations(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Routes(models.Model):
    destination_from = models.ForeignKey(Locations, models.CASCADE, related_name="destination_from")
    destination_to = models.ForeignKey(Locations, models.CASCADE, related_name="destination_to")
    distance = models.CharField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.destination_from} - {self.destination_to}"
    

class Shidule(models.Model):
    route = models.ForeignKey(Routes, models.CASCADE, related_name="route")
    time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.route.destination_from} - {self.route.destination_to} at {self.time}"
    

class Seats(models.Model):
    
    # toal_seats = models.PositiveIntegerField()
    A1 = models.BooleanField(default=False)
    A2 = models.BooleanField(default=False)
    B1 = models.BooleanField(default=False)
    B2 = models.BooleanField(default=False)
    C1 = models.BooleanField(default=False)
    C2 = models.BooleanField(default=False)
    D1 = models.BooleanField(default=False)
    D2 = models.BooleanField(default=False)
    E1 = models.BooleanField(default=False)
    E2 = models.BooleanField(default=False)
    
    
    
class Bus(models.Model):
    name = models.CharField(max_length=100)
    route = models.ForeignKey(Routes, models.CASCADE)
    shidule = models.ForeignKey(Shidule, models.CASCADE, related_name="shidule")
    seats = models.ForeignKey(Seats, models.CASCADE, related_name="seats", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    

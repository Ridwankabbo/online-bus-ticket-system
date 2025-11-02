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
    
    
    
class Bus(models.Model):
    name = models.CharField(max_length=100)
    route = models.ForeignKey(Routes, models.CASCADE)
    shidule = models.ForeignKey(Shidule, models.CASCADE, related_name="shidule")
    
    def __str__(self):
        return self.name
    
    

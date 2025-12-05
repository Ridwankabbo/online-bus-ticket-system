from django.db import models

# Create your models here.

class Locations(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Route(models.Model):
    source = models.ForeignKey(Locations, models.CASCADE, related_name='source_location')
    destination = models.ForeignKey(Locations, models.CASCADE, related_name='destination_location')
    destance = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f"{self.source} - {self.destination}"
    
class Bus(models.Model):
    class bus_type(models.TextChoices):
        AC = "AC", "ac"
        NON_AC = "NON_AC", "non_ac"
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=bus_type.choices, default=bus_type.NON_AC)
    
    def __str__(self):
        return f"{self.name}{self.pk} type: {self.type}"
    
    
class Seats(models.Model):
    bus = models.ForeignKey(Bus, models.CASCADE, related_name='bus')
    seat_name = models.CharField(max_length=2)
    seat_status=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.bus}   {self.seat_name}"
    
class Shidule(models.Model):
    route = models.ForeignKey(Route, models.CASCADE, related_name='bus_route')
    bus = models.ForeignKey(Bus, models.CASCADE, related_name='bus_shidule')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    bus_date_time = models.DateTimeField(blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.bus}  {self.route}  {self.bus_time}"
    
    

from django.db import models
from user.models import User
from bus.models import Shidule, Bus, Seats
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name='user')
    shidule = models.ForeignKey(Shidule, models.CASCADE, related_name='shidule')
    seats = models.JSONField(default=list)
    total_amount = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"custommer: {self.user.username}  shidule: {self.shidule} seats: {self.seats} created at: {self.created_at}"
    

from django.db import models
from Users.models import Users
from buses.models import Bus
# Create your models here.

class Bookings(models.Model):
    user = models.ForeignKey(Users, models.CASCADE, related_name="user")
    bus = models.ForeignKey(Bus, models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    
    booking_status_choices = [
        ("PENDING", "Pending"),
        ("CONFERMED","Confermed"),
        ("CANCLED", "Cancled")
    ]
    status = models.CharField(max_length=10, choices=booking_status_choices, default='PENDING')
    
    def __str__(self):
        return f"Booking {self.id} by {self.user.username} for{self.bus} from {self.booking_date}" 

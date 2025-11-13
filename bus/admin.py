from django.contrib import admin
from .models import (
    Locations,
    Route,
    Bus,
    Seats,
    Shidule
)
# Register your models here.
admin.site.register(Locations)
admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(Seats)
admin.site.register(Shidule)
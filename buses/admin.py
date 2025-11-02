from django.contrib import admin
from .models import(
    Locations,
    Routes,
    Shidule,
    Bus
)
# Register your models here.

admin.site.register(Locations)
admin.site.register(Routes)
admin.site.register(Shidule)
admin.site.register(Bus)

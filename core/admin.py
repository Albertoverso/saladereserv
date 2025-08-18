from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sala, Reserva

admin.site.register(Sala)
admin.site.register(Reserva)

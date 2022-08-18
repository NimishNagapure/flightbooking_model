from django.contrib import admin

# Register your models here.
from .models import FlightbookFlight,FlightbookReservation,FlightbookPassenger

admin.site.register(FlightbookPassenger)
admin.site.register(FlightbookReservation)
admin.site.register(FlightbookFlight)

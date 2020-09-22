from django.contrib import admin
from .models import BookingDate, BookingTime

# Register your models here.
admin.site.register(BookingDate)
admin.site.register(BookingTime)
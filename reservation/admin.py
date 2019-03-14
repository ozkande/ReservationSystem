from django.contrib import admin

# Register your models here.

from . models import Reservation, Table


admin.site.register(Reservation)
admin.site.register(Table)

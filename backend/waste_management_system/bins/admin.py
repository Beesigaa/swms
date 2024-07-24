from django.contrib import admin

# Register your models here.
# bins/admin.py
#from django.contrib import admin
from .models import Bin

#admin.site.register(Bin)

@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ('location', 'capacity', 'current_level', 'last_collected')


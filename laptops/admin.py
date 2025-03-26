from django.contrib import admin
from .models import Laptop

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'processor', 'ram', 'storage', 'display', 'graphics')
    list_filter = ('brand', 'price', 'processor', 'ram', 'storage', 'display', 'graphics')
    search_fields = ('brand', 'model', 'processor', 'display', 'graphics')
    ordering = ('price', 'brand', 'model')
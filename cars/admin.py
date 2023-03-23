from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    search_fields = ['make', 'model', 'displacement', 'year', 'is_supercharged', 'drag']
	
admin.site.register(Car, CarAdmin)
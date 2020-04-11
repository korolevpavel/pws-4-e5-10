from django.contrib import admin
from .models import Car, Color, Producer

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    
    list_display = ('producer', 'model_of_car', 'transmission', 'year',
                    'color')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    pass



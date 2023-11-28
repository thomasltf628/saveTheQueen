from django.contrib import admin
from .models import Todo, CarModel

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'model_name')

# Register your models here.

admin.site.register(Todo, TodoAdmin),
admin.site.register(CarModel, CarModelAdmin),
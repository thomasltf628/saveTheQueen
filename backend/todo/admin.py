from django.contrib import admin
from .models import Todo, Profile

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'picture')

# Register your models here.

admin.site.register(Todo, TodoAdmin),
admin.site.register(Profile, ProfileAdmin),
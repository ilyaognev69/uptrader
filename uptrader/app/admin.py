from django.contrib import admin
from .models import MenuItem
# Register your models here.

@admin.register(MenuItem)
class MenuItem(admin.ModelAdmin):
    list_display = ['name']
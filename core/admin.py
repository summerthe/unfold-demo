from django.contrib import admin
from .models import Driver
from unfold.admin import ModelAdmin


@admin.register(Driver)
class DriverAdmin(ModelAdmin):
    list_display = ("title",)
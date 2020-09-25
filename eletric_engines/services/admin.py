from django.contrib import admin
from .models import Services

# Register your models here.

@admin.register(Services)
class Services_admim(admin.ModelAdmin):
    list_display = ['id', 'address', 'stret', 'number', 'zipe_code', 'reference']

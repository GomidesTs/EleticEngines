from django.contrib import admin
from .models import Employyes

# Register your models here.

@admin.register(Employyes)
class Employyes_admim(admin.ModelAdmin):
    list_display = ['id', 'officce', 'shedule', 'salary', 'company_time', 'contract']

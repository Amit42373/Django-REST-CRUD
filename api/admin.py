from django.contrib import admin
from .models import Company, Employee

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("company_id", "name", "location", "active")


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee)

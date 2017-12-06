from django.contrib import admin

from .models import Report

# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_name', 'active')

admin.site.register(Report, ReportAdmin)
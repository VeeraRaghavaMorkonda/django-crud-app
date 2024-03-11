from django.contrib import admin
from .models import ServiceMappingModel
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(ServiceMappingModel)
class ServiceMappingAdmin(ImportExportModelAdmin):
    list_display = ()
    search_fields = ()
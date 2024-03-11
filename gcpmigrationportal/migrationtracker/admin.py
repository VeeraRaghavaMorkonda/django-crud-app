from django.contrib import admin
from .models import MigrationTrackerModel
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(MigrationTrackerModel)
class MigrationTrackierAdmin(ImportExportModelAdmin):
    list_display = ()
    search_fields = ()
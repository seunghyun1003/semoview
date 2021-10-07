from django.contrib import admin
from api.models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(User)
admin.site.register(Review)


@admin.register(StageData)
class StageDataAdmin(ImportExportModelAdmin):
    pass
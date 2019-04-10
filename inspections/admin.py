from django.contrib import admin
from .models import Inspector, OperationType, CityTown, inspectionsEstablishment, inspectionsEstablishmentInspectionReport

# Register your models here.
admin.site.register(Inspector)
admin.site.register(OperationType)
admin.site.register(CityTown)
admin.site.register(inspectionsEstablishment)
admin.site.register(inspectionsEstablishmentInspectionReport)
from django.contrib import admin
from .models import *


class PatientRecordInline(admin.StackedInline):
    model = PatientRecord
    extra = 0


class PatientAdmin(admin.ModelAdmin):
    inlines = [PatientRecordInline]
    list_display = ("name", "cc", "product_name")
    search_fields = ("name", "cc", "product_name__product_name")


class PatientRecordAdmin(admin.ModelAdmin):
    list_display = ("patient", "date")


class TraceabilityAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "purchase_date", "supplies")
    search_fields = ("invoice_number", "supplies")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name",)
    search_fields = ("product_name",)


class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ("raw_material_name",)


admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientRecord, PatientRecordAdmin)
admin.site.register(Traceability, TraceabilityAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(RawMaterial, RawMaterialAdmin)
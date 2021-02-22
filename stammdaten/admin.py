from django.contrib import admin
from .models import Firma, Kunde

class FirmaAdmin(admin.ModelAdmin):
    list_display = ('firma_name', 'image_thumb',)
    list_display_links = ('firma_name', 'image_thumb',)


admin.site.register(Firma, FirmaAdmin)
admin.site.register(Kunde)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Firma, Kunde, Firmenzugehörigkeit
from reklamation.models import Grund, Kategorie


class FirmaAdmin(admin.ModelAdmin):
    list_display = ('firma_name', 'image_thumb',)
    list_display_links = ('firma_name', 'image_thumb',)


class KundeAdmin(admin.ModelAdmin):
    list_display = ('id', 'lager_name',)
    list_display_links = ('id', 'lager_name',)


class BenutzerFirma(admin.StackedInline):
    model = Firmenzugehörigkeit
    can_delete = False
    verbose_name_plural = 'Firma'


class UserAdmin(BaseUserAdmin):
    inlines = (BenutzerFirma, )


admin.site.register(Firma, FirmaAdmin)
admin.site.register(Kunde, KundeAdmin)
admin.site.register(Grund)
admin.site.register(Kategorie)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

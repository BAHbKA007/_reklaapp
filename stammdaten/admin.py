from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Firma, Kunde, Firmenzugehörigkeit, FirmenBerechtigungen, KundenBerechtigungen
from reklamation.models import Grund, Kategorie


class FirmaAdmin(admin.ModelAdmin):
    list_display = ('firma_name', 'image_thumb',)
    list_display_links = ('firma_name', 'image_thumb',)
    filter_horizontal = ('firma_user',)


class KundeAdmin(admin.ModelAdmin):
    list_display = ('kunde_name', 'kunde_lager')
    list_display_links = ('kunde_name', 'kunde_lager',)


# Firmenfeld im User Admin Bereich erzeugen
class BenutzerFirma(admin.StackedInline):
    model = Firmenzugehörigkeit
    can_delete = False
    verbose_name_plural = 'Firma'


# Firmen dem User im User Admin Bereich zuordnen
class BenutzerFirmenBerechtigungen(admin.StackedInline):
    model = FirmenBerechtigungen
    can_delete = False
    verbose_name_plural = 'Firma'
    filter_horizontal = ('firma',)


# Kunde dem User im User Admin Bereich zuordnen
class BenutzerKundeBerechtigungen(admin.StackedInline):
    model = KundenBerechtigungen
    can_delete = False
    verbose_name_plural = 'Kunden'
    filter_horizontal = ('kunde',)


class UserAdmin(BaseUserAdmin):
    inlines = (
        BenutzerFirma,
        BenutzerFirmenBerechtigungen,
        BenutzerKundeBerechtigungen,)


admin.site.register(
    Firma,
    FirmaAdmin)
admin.site.register(
    Kunde,
    KundeAdmin)
admin.site.register(Grund)
admin.site.register(Kategorie)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(
    User,
    UserAdmin)

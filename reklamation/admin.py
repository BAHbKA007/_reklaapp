from django.contrib import admin
from .models import Reklamation

# class ReklamationAdmin(admin.ModelAdmin):
#     list_display = ('reklamation_name',)
#     list_display_links = ('reklamation_name',)

admin.site.register(Reklamation)

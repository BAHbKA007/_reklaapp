from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Firma(models.Model):
    firma_name = models.CharField(max_length=64, verbose_name='Firma')
    firma_logo = models.ImageField(upload_to='', blank=True, null=True)
    firma_created_at = models.DateTimeField(auto_now_add=True)
    firma_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firma_name
    
    # Bezeichnungen für Adminbereich
    class Meta:
        verbose_name = _("Firma")
        verbose_name_plural = _("Firmen")

    # Logo als Thumbnail im Adminbereich falls vorhanden
    def image_thumb(self):
        if self.firma_logo:
            return mark_safe('<img src="/media/{}" height="30"/>'.format(self.firma_logo))
        else:
            return 'kein Logo hochgeladen...'

    image_thumb.short_description = 'Logo'
    image_thumb.allow_tags = True

class Kunde(models.Model):
    kunde_name = models.CharField(max_length=64, verbose_name='Name')
    kunde_lager = models.CharField(max_length=64, verbose_name='Lager')
    kunde_created_at = models.DateTimeField(auto_now_add=True)
    kunde_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.kunde_name} {self.kunde_lager}"
    
    # Bezeichnungen für Adminbereich
    class Meta:
        verbose_name = _("Kunde")
        verbose_name_plural = _("Kunden")
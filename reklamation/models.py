from django.db import models
#from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from stammdaten.models import Firma, Grund, Kategorie, Kunde

# Create your models here.
class Reklamation(models.Model):

    reklamation_Datum = models.DateTimeField(verbose_name='Datum')
    reklamation_Lager= models.ForeignKey(Kunde, on_delete=models.DO_NOTHING, verbose_name='Lager',)
    reklamation_Firma= models.ForeignKey(Firma, on_delete=models.DO_NOTHING, verbose_name='Firma', blank=True, null=True)
    reklamation_User= models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Benutzer', blank=True, null=True)
    reklamation_Produkt = models.CharField(max_length=64, verbose_name='Produkt')
    reklamation_Menge = models.PositiveSmallIntegerField(verbose_name='Menge')
    reklamation_Grund= models.ForeignKey(Grund, on_delete=models.CASCADE, verbose_name='Grund', blank=True, null=True)
    reklamation_Kategorie= models.ForeignKey(Kategorie, on_delete=models.DO_NOTHING, verbose_name='Kategorie', blank=True, null=True)
    reklamation_Bemerkung = models.CharField(max_length=200, verbose_name='Bemerkung')
    reklamation_Maßnahmen = models.CharField(max_length=200, verbose_name='Maßnahmen')
    reklamation_Vertriebsmaßnahme = models.CharField(max_length=200, verbose_name='Vertriebsmaßnahme')
    reklamation_Lieferschein = models.CharField(max_length=64, verbose_name='Lieferschein')
    reklamation_Lieferant = models.CharField(max_length=64, verbose_name='Lieferant')
    reklamation_created_at = models.DateTimeField(auto_now_add=True)
    reklamation_updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} {}'.format(self.reklamation_Lager, self.reklamation_Produkt)
    
    # Bezeichnungen für Adminbereich
    class Meta:
        verbose_name = _("Reklamation")
        verbose_name_plural = _("Reklamationen")
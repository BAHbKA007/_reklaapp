from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from stammdaten.models import Firma, Kunde


class Kategorie(models.Model):
    kategorie_name = models.CharField(
        max_length=64,
        verbose_name='Kategorie')    
    kategorie_created_at = models.DateTimeField(auto_now_add=True)
    kategorie_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kategorie_name

    # Bezeichnungen für Adminbereich
    class Meta:
        verbose_name = _("Kategorie")
        verbose_name_plural = _("Kategorien")


class Grund(models.Model):
    grund_name = models.CharField(
        max_length=64,
        verbose_name='Grund')
    grund_created_at = models.DateTimeField(auto_now_add=True)
    grund_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grund_name

    # Bezeichnungen für Adminbereich
    class Meta:
        verbose_name = _("Grund")
        verbose_name_plural = _("Gründe")


class Reklamation(models.Model):
    reklamation_datum = models.DateTimeField(verbose_name='Datum')
    reklamation_lager = models.ForeignKey(
        Kunde,
        on_delete=models.DO_NOTHING,
        verbose_name='Lager',
        blank=True,
        null=True)
    reklamation_firma = models.ForeignKey(
        Firma,
        on_delete=models.DO_NOTHING,
        verbose_name='Firma',
        blank=True,
        null=True)
    reklamation_user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='Benutzer',
        blank=True,
        null=True)
    reklamation_produkt = models.CharField(
        max_length=64,
        verbose_name='Produkt')
    reklamation_menge = models.PositiveSmallIntegerField(verbose_name='Menge')
    reklamation_grund = models.ForeignKey(
        Grund,
        on_delete=models.CASCADE,
        verbose_name='Grund',
        blank=True,
        null=True)
    reklamation_kategorie = models.ForeignKey(
        Kategorie,
        on_delete=models.DO_NOTHING,
        verbose_name='Kategorie',
        blank=True,
        null=True)
    reklamation_bemerkung = models.CharField(
        max_length=200,
        verbose_name='Bemerkung')
    reklamation_maßnahmen = models.CharField(
        max_length=200,
        verbose_name='Maßnahmen')
    reklamation_vertriebsmaßnahme = models.CharField(
        max_length=200,
        verbose_name='Vertriebsmaßnahme')
    reklamation_lieferschein = models.CharField(
        max_length=64,
        verbose_name='Lieferschein')
    reklamation_lieferant = models.CharField(
        max_length=64,
        verbose_name='Lieferant')
    reklamation_created_at = models.DateTimeField(auto_now_add=True)
    reklamation_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.reklamation_Lager} {self.reklamation_Produkt}'

    # Bezeichnungen für Adminbereich
    class Meta:
        verbose_name = _("Reklamation")
        verbose_name_plural = _("Reklamationen")

from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Firma(models.Model):
    firma_name = models.CharField(max_length=64, verbose_name='Firma')
    firma_user = models.ManyToManyField(
        User,
        blank=True,
        null=True,
        verbose_name='User für die Firma berechtigen')
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
            return mark_safe(
                f'<img src="/media/{self.firma_logo}" height="30"/>')
        else:
            return 'kein Logo hochgeladen...'

    image_thumb.short_description = 'Logo'
    image_thumb.allow_tags = True


class Kunde(models.Model):
    kunde_name = models.CharField(
        max_length=64,
        verbose_name='Name')
    kunde_lager = models.CharField(
        max_length=64,
        verbose_name='Lager')
    kunde_user = models.ManyToManyField(
        User,
        blank=True,
        null=True,
        verbose_name='User für die Firma berechtigen')
    # kunde_user = models.ManyToManyField(
    #     User,
    #     blank=True,
    #     null=True,
    #     verbose_name='User für den Kunden berechtigen')
    kunde_created_at = models.DateTimeField(auto_now_add=True)
    kunde_updated_at = models.DateTimeField(auto_now=True)

    def lager_name(self):
        return f'{self.kunde_name} {self.kunde_lager}'

    def __str__(self):
        return f'{self.kunde_name} {self.kunde_lager}'

    # Bezeichnungen für Adminbereich
    class Meta:
        verbose_name = _("Kunde")
        verbose_name_plural = _("Kunden")


class Firmenzugehörigkeit(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Benutzer")
    firma = models.ForeignKey(
        Firma,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Firma')

    def __str__(self):
        return ''


class FirmenBerechtigungen(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Benutzer")
    firma = models.ManyToManyField(
        Firma,
        null=True,
        verbose_name='Firma')

    def __str__(self):
        return 'Firmen Berechtigungen'


class KundenBerechtigungen(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Benutzer")
    kunde = models.ManyToManyField(
        Kunde,
        null=True,
        verbose_name='Kunde')

    def __str__(self):
        return ''

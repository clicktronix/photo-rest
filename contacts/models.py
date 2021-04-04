"""Contacts model"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contacts(models.Model):
    """Contacts model class"""

    email = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="email"
    )
    phone = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="phone"
    )
    watsapp = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="watsapp"
    )
    instagram = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="instagram"
    )
    telegram = models.CharField(
        blank=True, null=True, max_length=255, verbose_name="telegram"
    )

    def save(self, *args, **kwargs):
        """
        Save only one contacts model instance
        """
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk

        super(Contacts, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Contacts")
        verbose_name_plural = _("Contacts")

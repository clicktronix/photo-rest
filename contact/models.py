"""Contact model"""
from django.db import models


class Contact(models.Model):
    """Contact model class"""

    email = models.CharField(blank=True, null=True, max_length=255)
    watsapp = models.CharField(blank=True, null=True, max_length=255)
    instagram = models.CharField(blank=True, null=True, max_length=255)
    phone = models.CharField(blank=True, null=True, max_length=255)

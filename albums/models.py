"""Photo model"""
from django.db import models


class Album(models.Model):
    """Album model class"""

    name = models.CharField(max_length=120, blank=False)
    description = models.TextField(max_length=300, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return u"%s" % (self.name)

"""Photo model"""
from django.db import models


class Photo(models.Model):
    """Photo model class"""

    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField()
    height = models.IntegerField()
    binary = models.ImageField(upload_to="photos/%Y.%m.%d", max_length=255, blank=True)
    album = models.TextField(max_length=100)
    is_grid = models.BooleanField(default=False)

    class Meta:
        ordering = ["created"]

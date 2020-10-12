"""Photo model"""
from django.db import models


class Photo(models.Model):
    """Photo model class"""

    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(max_length=10)
    height = models.IntegerField(max_length=10)
    src = models.CharField(max_length=100)
    album = models.TextField(max_length=100)
    is_grid = models.BooleanField(default=False)

    class Meta:
        ordering = ["created"]

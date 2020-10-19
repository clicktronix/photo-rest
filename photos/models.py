"""Photo model"""
from django.db import models


class Photo(models.Model):
    """Photo model class"""

    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField()
    height = models.IntegerField()
    img = models.ImageField(upload_to="photos", max_length=255, blank=True)
    is_grid = models.BooleanField(default=False)

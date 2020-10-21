"""Photo model"""
from django.db import models


class Photo(models.Model):
    """Photo model class"""

    created = models.DateTimeField(auto_now_add=True)
    width = models.PositiveIntegerField(editable=False)
    height = models.PositiveIntegerField(editable=False)
    img = models.ImageField(
        upload_to="photos", max_length=255, height_field="height", width_field="width"
    )
    is_grid = models.BooleanField(default=False)

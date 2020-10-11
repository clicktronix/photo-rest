from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    width = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    src = models.CharField(max_length=100)

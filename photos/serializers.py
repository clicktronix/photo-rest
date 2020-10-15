"""Serializers for photos"""
from rest_framework import serializers
from photos.models import Photo


class PhotoSerializer(serializers.Serializer):
    """Photo serializer class"""

    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    is_grid = serializers.BooleanField(required=False)

    class Meta:
        model = Photo
        fields = "__all__"

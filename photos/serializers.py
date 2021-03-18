"""Serializers for photos"""
from rest_framework import serializers
from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """Photo serializer class"""

    class Meta:
        """Meta class for Photo serializer"""

        model = Photo
        fields = "__all__"

"""Serializers for photos"""
from rest_framework import serializers
from photos.models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    """Photo serializer class"""

    class Meta:
        """Meta class for Photo serializer"""

        model = Photo
        fields = "__all__"


class AlbumSerializer():
    """Album serializer class"""

    class Meta:
        """Meta class for Album serializer"""

        model = Album
        fields = "__all__"

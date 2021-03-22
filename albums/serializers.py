"""Serializers for photos"""
from rest_framework import serializers
from photos.serializers import PhotoSerializer
from albums.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    """Album serializer class"""

    photos = PhotoSerializer(many=True, read_only=True)
    preview = PhotoSerializer(read_only=True)

    class Meta:
        """Meta class for Album serializer"""

        model = Album
        fields = ("id", "name", "description", "photos", "preview")

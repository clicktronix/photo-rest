"""Serializers for photos"""
from rest_framework import serializers
from photos.models import Album
from photos.serializers import PhotoSerializer


class AlbumSerializer(serializers.ModelSerializer):
    """Album serializer class"""

    photos = PhotoSerializer(many=True, read_only=True)
    preview = filter(lambda x: hasattr(x, 'is_album_preview'), photos.data[:])

    class Meta:
        """Meta class for Album serializer"""

        model = Album
        fields = ('name', 'description', 'photos', 'preview')

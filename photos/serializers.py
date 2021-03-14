"""Serializers for photos"""
from rest_framework import serializers
from photos.models import Photo, Album


class PhotoSerializer(serializers.ModelSerializer):
    """Photo serializer class"""

    class Meta:
        """Meta class for Photo serializer"""

        model = Photo
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    """Album serializer class"""

    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        """Meta class for Album serializer"""

        model = Album
        fields = ('name', 'description', 'photos')

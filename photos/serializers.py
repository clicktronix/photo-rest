"""Serializers for photos"""
from rest_framework import serializers
from photos.models import Photo


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Photo serializer class"""

    class Meta:
        model = Photo
        fields = "__all__"

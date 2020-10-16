"""Views for photos"""
from rest_framework import generics
from photos.serializers import PhotoSerializer


class PhotoListView(generics.ListAPIView):
    """Photo list view class"""

    serializer_class = PhotoSerializer


class PhotoCreateView(generics.CreateAPIView):
    """Photo create view class"""

    serializer_class = PhotoSerializer

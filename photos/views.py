"""Views for photos"""
from rest_framework import generics
from photos.serializers import PhotoSerializer
from photos.models import Photo


class PhotoListView(generics.ListAPIView):
    """Photo list view class"""

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoCreateView(generics.CreateAPIView):
    """Photo create view class"""

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

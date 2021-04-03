"""Views for photos"""
from rest_framework import generics
from photos.serializers import PhotoSerializer
from photos.models import Photo


class PhotoListGridView(generics.ListAPIView):
    """Photo list view class"""

    queryset = Photo.objects.filter(is_grid=True)
    serializer_class = PhotoSerializer


class PhotoListMainScreenView(generics.ListAPIView):
    """Photo list view class"""

    queryset = Photo.objects.filter(is_main_screen=True)
    serializer_class = PhotoSerializer


class PhotoAboutRetrieveView(generics.RetrieveAPIView):
    """Photo list view class"""

    queryset = Photo.objects.filter(is_about_preview=True)
    serializer_class = PhotoSerializer


class PhotoRetrieveView(generics.RetrieveAPIView):
    """Photo retrieve view class"""

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

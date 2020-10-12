"""Views for photos"""
from rest_framework import generics
from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotosListView(generics.ListAPIView):
    """Photo list view class"""

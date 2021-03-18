"""Views for photos"""
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
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


class PhotoCreateView(generics.CreateAPIView):
    """Photo create view class"""

    parser_classes = (MultiPartParser, FormParser)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer(queryset, many=True)

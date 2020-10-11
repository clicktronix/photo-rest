from django.shortcuts import render
from rest_framework import generics
from photos.models import Photos
from photos.serializers import PhotoSerializer


class PhotosListView(generics.ListAPIView):
    serializer_class = PhotoSerializer
    queryset = Photos.objects.all()

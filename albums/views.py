"""Views for albums"""
from rest_framework import generics
from albums.models import Album
from albums.serializers import AlbumSerializer


class AlbumListView(generics.ListAPIView):
    """Album list view class"""

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumCreateView(generics.RetrieveAPIView):
    """Album  create view class"""

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

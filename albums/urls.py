"""Albums app urls"""
from django.urls import path
from albums.views import AlbumListView

app_name = "albums"

urlpatterns = [
    path("", AlbumListView.as_view()),
]

"""Albums app urls"""
from django.urls import path
from albums.views import AlbumListView, AlbumCreateView

app_name = "albums"

urlpatterns = [
    path("", AlbumListView.as_view()),
    path("<int:id>/", AlbumCreateView.as_view()),
]

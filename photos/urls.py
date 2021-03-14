"""Photo app urls"""
from django.urls import path
from photos.views import PhotoCreateView, PhotoListGridView, PhotoListMainScreenView, AlbumListView

app_name = "photo"

urlpatterns = [
    path("<int:id>/", PhotoCreateView.as_view()),
    path("grid", PhotoListGridView.as_view()),
    path("main-screen", PhotoListMainScreenView.as_view()),
    path("albums/<int:id>/", AlbumListView.as_view()),
]

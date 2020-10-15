"""Photo app urls"""
from django.urls import path
from photos.views import PhotosCreateView, PhotosListView

urlpatterns = [
    path("photo/<int:id>/", PhotosCreateView.as_view()),
    path("photo/", PhotosListView.as_view()),
]

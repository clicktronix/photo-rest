"""Photo app urls"""
from django.urls import path
from photos.views import PhotoCreateView, PhotoListView

app_name = "photo"
urlpatterns = [
    path("photos/<int:id>/", PhotoCreateView.as_view()),
    path("photos/", PhotoListView.as_view()),
]

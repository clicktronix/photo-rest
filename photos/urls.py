"""Photo app urls"""
from django.urls import path
from photos.views import PhotoCreateView, PhotoListView

app_name = "photo"

urlpatterns = [
    path("<int:id>/", PhotoCreateView.as_view()),
    path("", PhotoListView.as_view()),
]

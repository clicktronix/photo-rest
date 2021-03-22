"""Photo app urls"""
from django.urls import path
from photos.views import PhotoRetrieveView, PhotoListGridView, PhotoListMainScreenView

app_name = "photos"

urlpatterns = [
    path("<int:pk>", PhotoRetrieveView.as_view()),
    path("grid", PhotoListGridView.as_view()),
    path("main-screen", PhotoListMainScreenView.as_view()),
]

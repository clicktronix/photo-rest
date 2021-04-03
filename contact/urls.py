"""Contact app urls"""
from django.urls import path
from contact.views import ContactRetrieveView

app_name = "contact"

urlpatterns = [
    path("", ContactRetrieveView.as_view()),
]

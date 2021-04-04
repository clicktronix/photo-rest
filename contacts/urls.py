"""Contact app urls"""
from django.urls import path
from contacts.views import ContactsRetrieveView

app_name = "contacts"

urlpatterns = [
    path("", ContactsRetrieveView.as_view({"get": "list"})),
]

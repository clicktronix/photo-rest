"""Contact view class"""
from rest_framework import generics
from contact.models import Contact
from contact.serializers import ContactSerializer


class ContactRetrieveView(generics.RetrieveAPIView):
    """Contact retrieve view class"""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

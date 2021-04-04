"""Contact view class"""
from rest_framework import viewsets
from rest_framework.response import Response
from contacts.models import Contacts
from contacts.serializers import ContactsSerializer


class ContactsRetrieveView(viewsets.ViewSet):
    """Contacts retrieve view class"""

    def list(self, request):
        """Return the first item in the list"""
        queryset = Contacts.objects.all()
        serializer = ContactsSerializer(queryset, many=True)
        if serializer.data:
            return Response(serializer.data[0])
        return Response("No contact data")

"""Serializers for photos"""
from rest_framework import serializers
from contacts.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    """Contacts serializer class"""

    class Meta:
        """Meta class for Contacts serializer"""

        model = Contacts
        fields = "__all__"

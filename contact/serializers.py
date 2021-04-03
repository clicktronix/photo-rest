"""Serializers for photos"""
from rest_framework import serializers
from contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Contact serializer class"""

    class Meta:
        """Meta class for Contact serializer"""

        model = Contact
        fields = "__all__"

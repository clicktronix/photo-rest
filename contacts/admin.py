"""Admin for contact app"""
from django.contrib import admin
from contacts.models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """Class for customizing admins contacts view"""

    list_display = (
        "email",
        "whatsapp",
        "instagram",
        "phone",
    )

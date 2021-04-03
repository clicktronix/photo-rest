"""Admin for contact app"""
from django.contrib import admin
from contact.models import Contact


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    """Class for customizing admins contact view"""

    list_display = (
        "email",
        "watsapp",
        "instagram",
        "phone",
    )

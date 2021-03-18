"""Admin for albums app"""
from django.contrib import admin
from django.utils.html import format_html
from albums.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Class for customizing admins albums view"""

    list_display = ("id", "name", "description", "preview")

    def preview(self, obj):
        """Format album photo preview"""
        return format_html(
            '<img src="/media/{}" style="width: 130px; height: auto"/>'.format(obj.preview)
        )

    preview.short_description = 'preview'

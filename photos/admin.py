"""Admin for photos app"""
from django.contrib import admin
from django.utils.html import format_html
from photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Class for customizing admins photos view"""

    list_display = (
        "id",
        "src",
        "is_grid",
        "is_main_screen",
        "is_album_preview",
        "thumbnail",
    )

    def thumbnail(self, obj):
        """Format html image preview"""
        return format_html(
            '<img src="/media/{}" style="width: 130px; height: auto"/>'.format(obj.src)
        )

    thumbnail.short_description = "thumbnail"

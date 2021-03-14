"""Admin for photos app"""
from django.contrib import admin
from django.utils.html import format_html
from photos.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    """Class for customizing admins view"""

    list_display = ("id", "img", "is_grid", "is_main_screen", "thumbnail")

    def thumbnail(self, obj):
        """Format html image preview"""
        return format_html(
            '<img src="/media/{}" style="width: 130px; height: auto"/>'.format(obj.img)
        )

    thumbnail.short_description = 'thumbnail'


# Register your models here.
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album)

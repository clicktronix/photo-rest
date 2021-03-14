"""Admin for photos app"""
from django.contrib import admin
from photos.models import Photo, Album
from django.utils.html import format_html


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "img", "thumbnail")

    def thumbnail(self, obj):
        return format_html('<img src="/media/{}" style="width: 130px; height: auto"/>'.format(obj.img))

    thumbnail.short_description = 'thumbnail'


# Register your models here.
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album)

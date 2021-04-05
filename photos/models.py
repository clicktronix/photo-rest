"""Photo model"""
import sys
from io import BytesIO
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from albums.models import Album


class Photo(models.Model):
    """Photo model class"""

    created = models.DateTimeField(auto_now_add=True)
    width = models.PositiveIntegerField(editable=False)
    height = models.PositiveIntegerField(editable=False)
    src = models.ImageField(
        upload_to="photos", max_length=255, height_field="height", width_field="width"
    )
    is_grid = models.BooleanField(default=False)
    is_main_screen = models.BooleanField(default=False)
    is_about_preview = models.BooleanField(default=False)
    album_id = models.ForeignKey(
        Album, related_name="photos", on_delete=models.CASCADE, blank=True, null=True
    )
    album_preview = models.OneToOneField(
        Album,
        related_name="preview",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        """
        Custom save method with photo compressing
        """
        ratio = 0.8
        blob = BytesIO()
        self.src.open()
        photo = Image.open(self.src)
        photo = photo.resize([int(ratio * s) for s in photo.size], Image.ANTIALIAS)
        photo.save(blob, "JPEG", quality=70, optimize=True)
        blob.seek(0)
        self.src = InMemoryUploadedFile(
            blob,
            "ImageField",
            "%s.jpg" % self.src.name.split(".")[0],
            "image/jpeg",
            sys.getsizeof(blob),
            None,
        )
        if self.is_about_preview:
            items = Photo.objects.filter(is_about_preview=True)
            for item in items:
                item.is_about_preview = False
                item.save()
        super(Photo, self).save(*args, **kwargs)


@receiver(post_delete, sender=Photo)
def submission_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem
    when corresponding `Photo` object is deleted.
    """
    instance.src.delete(False)


@receiver(pre_save, sender=Photo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem
    when corresponding `Photo` object is updated
    with new image.
    """
    if not instance.pk:
        return False

    try:
        old_img = Photo.objects.get(pk=instance.pk).src
    except Photo.DoesNotExist:
        return False

    new_img = instance.src

    if not old_img == new_img:
        old_img.delete(False)
        return True

    return False

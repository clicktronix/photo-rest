"""Photo model"""
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class Album(models.Model):
    """Album model class"""

    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(max_length=300, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return u'%s' % (self.name)


class Photo(models.Model):
    """Photo model class"""

    created = models.DateTimeField(auto_now_add=True)
    width = models.PositiveIntegerField(editable=False)
    height = models.PositiveIntegerField(editable=False)
    img = models.ImageField(
        upload_to="photos", max_length=255, height_field="height", width_field="width"
    )
    album_id = models.ForeignKey(
        Album, related_name='photos', on_delete=models.CASCADE, blank=True, null=True
    )
    is_grid = models.BooleanField(default=False)
    is_main_screen = models.BooleanField(default=False)
    readonly_fields = ('image_preview', )



@receiver(post_delete, sender=Photo)
def submission_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem
    when corresponding `Photo` object is deleted.
    """
    instance.img.delete(False)


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
        old_img = Photo.objects.get(pk=instance.pk).img
    except Photo.DoesNotExist:
        return False

    new_img = instance.img
    if not old_img == new_img:
        old_img.delete(False)


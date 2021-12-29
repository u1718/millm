from django.db import models

#am#from taggit.managers import TaggableManager

from photologue.models import IMAGE_FIELD_MAX_LENGTH, get_storage_path 
from django.utils.translation import gettext_lazy as _
from photologue.models import Gallery, Photo


class GalleryExtended(models.Model):

    # Link back to Photologue's Gallery model.
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE, related_name='extended')

    #am## This is the important bit - where we add in the tags.
    #am#tags = TaggableManager(blank=True)
    #breakpoint()
    image = models.ImageField(_('image'),
                              default=None,
                              max_length=IMAGE_FIELD_MAX_LENGTH,
                              upload_to=get_storage_path)
    # Boilerplate code to make a prettier display in the admin interface.
    class Meta:
        verbose_name = u'Extra fields'
        verbose_name_plural = u'Extra fields'

    def __str__(self):
        return self.gallery.title

class PhotoExtended(models.Model):

    # Link back to Photologue's Gallery model.
    photo = models.OneToOneField(Photo, on_delete=models.CASCADE, related_name='extended')

    image = models.ImageField(_('image'),
                              default=None,
                              max_length=IMAGE_FIELD_MAX_LENGTH,
                              upload_to=get_storage_path)
    # Boilerplate code to make a prettier display in the admin interface.
    class Meta:
        verbose_name = u'Extra fields'
        verbose_name_plural = u'Extra fields'

    def __str__(self):
        return self.photo.title

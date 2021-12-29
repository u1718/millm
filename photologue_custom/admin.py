from django.contrib import admin

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.admin import PhotoAdmin as PhotoAdminDefault
from photologue.models import Gallery, Photo
from .models import GalleryExtended, PhotoExtended


class GalleryExtendedInline(admin.StackedInline):
    model = GalleryExtended
    can_delete = False


class GalleryAdmin(GalleryAdminDefault):

    """Define our new one-to-one model as an inline of Photologue's Gallery model."""

    inlines = [GalleryExtendedInline, ]

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)

class PhotoExtendedInline(admin.StackedInline):
    model = PhotoExtended
    can_delete = False


class PhotoAdmin(PhotoAdminDefault):

    inlines = [PhotoExtendedInline, ]

admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)

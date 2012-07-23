import os, unicodedata

from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.core.files.storage import FileSystemStorage
from django.db.models.fields.files import FileField
from django.core.files.storage import default_storage

from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.exceptions import InvalidImageFormatError


class AdminThumbnailMixin(object):
    thumbnail_options = {'size': (60, 60)}
    thumbnail_image_field_name = 'image'
    thumbnail_alt_field_name = None
    thumbnail_404 = ""

    def _thumb(self, image, options={'size': (60, 60)}, alt=None):
        media = getattr(settings, 'THUMBNAIL_MEDIA_URL', settings.MEDIA_URL)
        attrs = []
        try:
            src = "%s%s" % (media, get_thumbnailer(image).get_thumbnail(options))
        except InvalidImageFormatError:
            src = self.thumbnail_404
        if alt is not None: attrs.append('alt="%s"' % alt)

        return mark_safe('<img src="%s" %s />' % (src, " ".join(attrs)))

    def thumbnail(self, obj):
        kwargs = {'options': self.thumbnail_options}
        if self.thumbnail_alt_field_name:
            kwargs['alt'] = getattr(obj, self.thumbnail_alt_field_name)
        return self._thumb(getattr(obj, self.thumbnail_image_field_name), **kwargs)
    thumbnail.allow_tags = True
    thumbnail.short_description = _('Thumbnail')


def file_cleanup(sender, **kwargs):
    """
    File cleanup callback used to emulate the old delete
    behavior using signals. Initially django deleted linked
    files when an object containing a File/ImageField was deleted.

    Usage:

    >>> from django.db.models.signals import post_delete

    >>> post_delete.connect(file_cleanup, sender=MyModel, dispatch_uid="mymodel.file_cleanup")
    """
    for fieldname in sender._meta.get_all_field_names():
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None
        if field and isinstance(field, FileField):
            inst = kwargs['instance']
            f = getattr(inst, fieldname)
            m = inst.__class__._default_manager
            if hasattr(f, 'path') and os.path.exists(f.path) \
                and not m.filter(**{'%s__exact' % fieldname: getattr(inst, fieldname)})\
                .exclude(pk=inst._get_pk_val()):
                    try:
                        #os.remove(f.path)
                        default_storage.delete(f.path)
                    except:
                        pass


class ASCIISafeFileSystemStorage(FileSystemStorage):
    """
    Same as FileSystemStorage, but converts unicode characters
    in file name to ASCII characters before saving the file. This
    is mostly useful for the non-English world.

    Usage (settings.py):

    >>> DEFAULT_FILE_STORAGE = 'automatix.utils.ASCIISafeFileSystemStorage'
    """

    def get_valid_name(self, name):
        name = unicodedata.normalize('NFKD', unicode(name.replace(' ', '_'))).encode('ascii', 'ignore')
        return super(ASCIISafeFileSystemStorage, self).get_valid_name(name)



from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete

from easy_thumbnails.fields import ThumbnailerImageField
from company.conf import settings
from company.utils import file_cleanup


class Company(models.Model):
    name = models.CharField(_('Name'), max_length=settings.MAX_NAME_LENGTH, 
            blank=True, null=True)
    slug = models.SlugField(_('Slug'), unique=True, 
            max_length=settings.MAX_SLUG_LENGTH)
    logo = ThumbnailerImageField(_('Logo'), upload_to='company/logo/', 
            resize_source=dict(size=settings.LOGO_MAX_SIZE), blank=True, null=True)
    slogan = models.CharField(_('Slogan'), max_length=250, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        app_label = 'company'
        ordering = ('name',)
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

post_delete.connect(file_cleanup, sender=Company, 
        dispatch_uid="Company.file_cleanup")

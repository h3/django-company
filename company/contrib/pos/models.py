from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete

from easy_thumbnails.fields import ThumbnailerImageField

from company.conf import settings
from company.utils import file_cleanup
from company.models import Company


class PointOfService(models.Model):
    name       = models.CharField(_('Name'), max_length=settings.MAX_NAME_LENGTH, blank=True, null=True)
    slug       = models.SlugField(_('Slug'), unique=True, max_length=settings.MAX_SLUG_LENGTH)
    photo      = ThumbnailerImageField(_('Photo'), upload_to='company/pos/', resize_source=dict(size=settings.LOGO_MAX_SIZE), blank=True, null=True)
    company    = models.ForeignKey(Company, blank=True, null=True)
    street_num = models.CharField(_('Street number'), max_length=20, blank=True, null=True)
    street     = models.CharField(_('Street'), max_length=150,  blank=True, null=True)
    city       = models.CharField(_('City'), max_length=150, blank=True, null=True)
    state      = models.CharField(_('State or province'), max_length=150, blank=True, null=True)
    country    = models.CharField(_('Country'), max_length=150, blank=True, null=True)
    zipcode    = models.CharField(_('Postal code'), max_length=50, blank=True, null=True)
    gmap       = models.TextField(_('Google Map'), blank=True, null=True)
    phone      = models.CharField(_('Phone'), max_length=60, blank=True, null=True)
    tollfree   = models.CharField(_('Toll-free'), max_length=60, blank=True, null=True)
    fax        = models.CharField(_('Fax'), max_length=60, blank=True, null=True)
    position   = models.PositiveIntegerField(_('Position'), default=0)
    is_visible = models.BooleanField(_('Is visible'), default=True)

    class Meta:
        app_label = 'company'
        ordering = ('position', 'name')
        verbose_name = _('Point of service')
        verbose_name_plural = _('Points of service')

    def __unicode__(self):
        return unicode(self.name)

post_delete.connect(file_cleanup, sender=PointOfService, 
        dispatch_uid="PointOfService.file_cleanup")

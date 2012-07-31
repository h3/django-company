from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete

from easy_thumbnails.fields import ThumbnailerImageField
from company.conf import settings
from company.utils import file_cleanup


class Testimonial(models.Model):
    firstname  = models.CharField(_('Firstname'), max_length=60)
    lastname   = models.CharField(_('Lastname'), max_length=60)
    title      = models.CharField(_('Job title'), max_length=60, blank=True, null=True)
    company    = models.CharField(_('Company'), max_length=100, blank=True, null=True)
    location   = models.CharField(_('Location'), max_length=100, blank=True, null=True)
    image      = ThumbnailerImageField(_('Image'), upload_to='company/testimonials/', 
                    resize_source=dict(size=settings.LOGO_MAX_SIZE), blank=True, null=True)
    website    = models.URLField(_('Website'), max_length=250, blank=True, null=True)
    text       = models.TextField(_('Bio'), blank=True, null=True)
    position   = models.PositiveIntegerField(_('Position'), default=0)
    is_visible = models.BooleanField(_('Is visible'), default=True)

    def __unicode__(self):
        return _("Testimonial of %(name)s from %(company)s") % {
                'name': self.firstname +' '+ self.lastname, 
                'company': self.company}

    class Meta:
        app_label = 'company'
        ordering = ('position', 'firstname', 'lastname')
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

post_delete.connect(file_cleanup, sender=Testimonial, 
        dispatch_uid="Testimonial.file_cleanup")

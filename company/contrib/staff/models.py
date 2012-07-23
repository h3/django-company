from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete

from easy_thumbnails.fields import ThumbnailerImageField
from company.conf import settings
from company.utils import file_cleanup


class Employee(models.Model):
    firstname  = models.CharField(_('Firstname'), max_length=60)
    lastname   = models.CharField(_('Lastname'), max_length=60)
    title      = models.CharField(_('Job title'), max_length=60, blank=True, null=True)
    photo      = ThumbnailerImageField(_('Photo'), upload_to='company/employees/', 
                    resize_source=dict(size=settings.LOGO_MAX_SIZE), blank=True, null=True)
    email      = models.EmailField(_('Email'), max_length=250, blank=True, null=True)
    work_phone = models.CharField(_('Work phone'), max_length=60, blank=True, null=True)
    cell_phone = models.CharField(_('Cell. phone'), max_length=60, blank=True, null=True)
    home_phone = models.CharField(_('Home phone'), max_length=60, blank=True, null=True)
    mike_phone = models.CharField(_('Mike phone'), max_length=60, blank=True, null=True)
    pager      = models.CharField(_('Pager'), max_length=60, blank=True, null=True)
    fax        = models.CharField(_('Fax'), max_length=60, blank=True, null=True)
    bio        = models.TextField(_('Bio'), blank=True, null=True)
    position   = models.PositiveIntegerField(_('Position'), default=0)
    is_visible = models.BooleanField(_('Is visible'), default=True)

    def __unicode__(self):
        return u"%s %s" % (self.firstname, self.lastname)

    class Meta:
        app_label = 'company'
        ordering = ('position', 'firstname', 'lastname')
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

post_delete.connect(file_cleanup, sender=Employee, 
        dispatch_uid="Employee.file_cleanup")

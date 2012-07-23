from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete

from easy_thumbnails.fields import ThumbnailerImageField
from company.conf import settings
from company.utils import file_cleanup

class AddressBase(models.Model):
    street_number = models.CharField(_('Address'), max_length=20, 
                        blank=True, null=True)
    street = models.CharField(_('Address'), max_length=150, 
                blank=True, null=True)
    city   = models.CharField(_('City'), max_length=150, 
                blank=True, null=True)
    state  = models.CharField(_('State or province'), max_length=150, 
                blank=True, null=True)
    country = models.CharField(_('Country'), max_length=150, 
                 blank=True, null=True)


class Company(AddressBase):
    name = models.CharField(_('Name'), max_length=settings.MAX_NAME_LENGTH, 
            blank=True, null=True)
    slug = models.SlugField(_('Slug'), unique=True, 
            max_length=settings.MAX_SLUG_LENGTH)
    logo = ThumbnailerImageField(_('Photo'), upload_to='slider-images/', 
            resize_source=dict(size=settings.LOGO_MAX_SIZE))
    slogan = models.CharField(_('Slogan'), max_length=250, blank=True, null=True)

post_delete.connect(file_cleanup, sender=SliderImage, 
        dispatch_uid="SliderImage.file_cleanup")


class PointOfService(AddressBase):
    name  = models.CharField(_('Name'), max_length=settings.MAX_NAME_LENGTH, 
                blank=True, null=True)
    slug  = models.SlugField(_('Slug'), unique=True, 
                max_length=settings.MAX_SLUG_LENGTH)
    photo = ThumbnailerImageField(_('Photo'), upload_to='company/pos/', 
                resize_source=dict(size=settings.LOGO_MAX_SIZE))
    gmap = models.CharField(_('Google Map'), blank=True, null=True)
    is_visible = models.BooleanField(_('Is visible'), default=True)


class Employee(models.Model):
    # firstname
    # lastname
    # job title
    # email
    # work phone
    # cell phone
    # home phone
    # mike
    # pager
    # bio
    # is active
    # is visible

    pass

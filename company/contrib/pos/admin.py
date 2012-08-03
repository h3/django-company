# -*- coding: utf-8 -*-

from django.contrib import admin
#from django.utils.translation import ugettext_lazy as _
from webcore.utils.admin import AdminThumbnailMixin
from grappellifit.admin import TranslationAdmin
from company.contrib.pos.models import PointOfService


class PointOfServiceAdmin(AdminThumbnailMixin, TranslationAdmin):
    list_display = ('thumbnail', 'name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    thumbnail_options = {'size': (80, 80)}
    thumbnail_image_field_name = 'photo'
    thumbnail_alt_field_name = 'name'
    thumbnail_404 = ""
admin.site.register(PointOfService, PointOfServiceAdmin)
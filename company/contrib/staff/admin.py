# -*- coding: utf-8 -*-

from django.contrib import admin
#from django.utils.translation import ugettext_lazy as _
from webcore.utils.admin import AdminThumbnailMixin
from grappellifit.admin import TranslationAdmin
from company.contrib.staff.models import Employee


class EmployeeAdmin(AdminThumbnailMixin, TranslationAdmin):
    list_display = ('thumbnail', 'firstname', 'lastname', 'title', 'is_visible')
    thumbnail_options = {'size': (100,100), 'crop': True}
    thumbnail_image_field_name = 'photo'
admin.site.register(Employee, EmployeeAdmin)

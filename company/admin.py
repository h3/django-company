# -*- coding: utf-8 -*-

from django.contrib import admin
#from django.utils.translation import ugettext_lazy as _
from webcore.utils.admin import AdminThumbnailMixin
from grappellifit.admin import TranslationAdmin
from company.models import Company


class CompanyAdmin(AdminThumbnailMixin, TranslationAdmin):
    list_display = ('thumbnail', 'name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Company, CompanyAdmin)

# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
#from django.utils.translation import ugettext_lazy as _
from webcore.utils.admin import AdminThumbnailMixin
from grappellifit.admin import TranslationAdmin

from company.contrib.testimonials.models import Testimonial


class TestimonialAdmin(AdminThumbnailMixin, TranslationAdmin):
    list_display = ('thumbnail', 'firstname', 'lastname', 'title', 'company', 'website', 'is_visible')
    thumbnail_options = {'size': (150, 150), 'crop': True}
    thumbnail_alt_field_name = 'company'
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/website/js/tinymce_setup.js',
        ]

admin.site.register(Testimonial, TestimonialAdmin)

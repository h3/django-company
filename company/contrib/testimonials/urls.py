# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic import ListView

from company.contrib.testimonials.views import TestimonialListView

urlpatterns=patterns('',
    url(r'^$', TestimonialListView.as_view(), name='company-testimonials-list'),
)

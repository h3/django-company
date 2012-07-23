# -*- coding: utf-8 -*-

from django.views.generic import ListView
from company.contrib.testimonials.models import Testimonial


class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'company/testimonials/testimonial_list.html'

    def get_queryset(self):
        return self.model.objects.filter(is_visible=True)

import os
#import datetime

from django.core.urlresolvers import reverse
from django import template

from company.contrib.testimonials.models import Testimonial

register = template.Library()


@register.assignment_tag
def get_testimonials(*args, **kwargs):
    """
    Returns a sorted list of testimonials

    {% get_testimonials limit=10 shuffle="true" as testimonials_list %}
    """
    limit   = kwargs.get('limit', None)
    shuffle = kwargs.get('shuffle', None)
    qs      = Testimonial.objects.filter(is_visible=True)

    if shuffle: qs = qs.order_by('?')

    return limit and qs[0:limit] or qs


@register.assignment_tag
def get_random_testimonial(*args, **kwargs):
    """
    Returns a random testimonial

    {% get_random_testimonial as testimonial %}
    """
    try:
        return Testimonial.objects.order_by('?').filter(is_visible=True)[0]
    except:
        return None

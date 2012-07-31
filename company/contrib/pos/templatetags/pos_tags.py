import os

from django.core.urlresolvers import reverse
from django import template

from company.contrib.pos.models import PointOfService

register = template.Library()


@register.assignment_tag
def get_pos_list(*args, **kwargs):
    """
    Returns a sorted list of point of services

    {% get_pos_list limit=10 as pos_list %}
    """
    limit   = kwargs.get('limit', None)
    qs      = PointOfService.objects.filter(is_visible=True)

    return limit and qs[0:limit] or qs


@register.assignment_tag
def get_pos(slug, *args, **kwargs):
    """
    Returns a point of services

    {% get_pos "my-pos" as pos %}
    """
    return PointOfService.objects.get(slug=slug)

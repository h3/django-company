import os

from django.core.urlresolvers import reverse
from django import template

from company.contrib.staff.models import Employee

register = template.Library()


@register.assignment_tag
def get_staff_list(*args, **kwargs):
    """
    Returns a sorted list of testimonials

    {% get_staff_list limit=10 as staff_list %}
    """
    limit   = kwargs.get('limit', None)
    qs      = Employee.objects.filter(is_visible=True)

    return limit and qs[0:limit] or qs

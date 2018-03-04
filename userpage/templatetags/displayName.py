from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='displayName')
@stringfilter
def displayName(value, arg):
    return eval('value.get_'+arg+'_display()')

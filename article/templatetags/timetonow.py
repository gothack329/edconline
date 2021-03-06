from django import template
from django.template.defaultfilters import stringfilter
import datetime
from django.utils import timezone

register = template.Library()

@register.filter
@stringfilter
def timetonow(value):
    # value: 2018-02-28 07:53:04.802169+00:00
    valuetime = datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f+00:00")
    now = timezone.now()
    now = now.replace(tzinfo=None)
    delta = now-valuetime

    s = delta.total_seconds()
    if s>86400:
        if int(s%86400/3600) == 0:
            return  '%d天前' % (int(s/86400))
        else:
           return '%d天%d小时前' % (int(s/86400),s%86400/3600)
    elif s>3600:
        return '%d小时前' % (int(s/3600))
    elif s>120:
        return '%d分钟前' % (int(s/60))
    else:
        return '刚刚' 

timetonow.is_safe = True
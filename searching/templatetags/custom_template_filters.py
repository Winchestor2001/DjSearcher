from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def timesince_uz(date):
    now = datetime.now()
    date = datetime.strptime(date.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    difference = now - date
    if difference <= timedelta(minutes=1):
        return 'hozir'
    elif difference <= timedelta(hours=1):
        minutes = int(difference.total_seconds() / 60)
        return f'{minutes} minut oldin'
    elif difference <= timedelta(days=1):
        hours = int(difference.total_seconds() / 3600)
        return f'{hours} soat oldin'
    else:
        days = int(difference.total_seconds() / 86400)
        return f'{days} kun oldin'


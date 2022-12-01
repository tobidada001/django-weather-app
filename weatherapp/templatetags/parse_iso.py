from django.template import Library
import datetime

register = Library()

@register.filter(expects_localtime=True)
def parse_iso(value):
    return datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


@register.filter
def get_item(myList, index=0):
    
    if index < 0:
        return myList[0]
    else:
        return myList[index]
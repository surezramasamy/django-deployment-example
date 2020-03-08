from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts overall values of "arg" from string
    """
    return value.replace(arg,'')

register.filter('cut',cut)

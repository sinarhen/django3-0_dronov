from django import template

register = template.Library()


@register.filter(name='currency')
def currency(value, name='grn'):
    return f'{value, name}'

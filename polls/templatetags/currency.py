from django import template
from django.contrib.humanize.templatetags.humanize import intcomma


register = template.Library()


@register.filter_function
def currency(dollars):
    dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])


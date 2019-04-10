from django import template

register = template.Library()

'''
  Used by navigation in base.html to attach the 'active' class to links
  @ref https://stackoverflow.com/a/477719/7799574
'''
@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''
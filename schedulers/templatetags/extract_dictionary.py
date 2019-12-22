from django import template

import ast
register = template.Library()

@register.filter(name='extract_dict')
def extract_dict(v):
    try:
        ch = ast.literal_eval(str(v))
        ch = ch['alert']
    except Exception as e:
        ch = None
    
    return ch

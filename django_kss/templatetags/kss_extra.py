from django import template
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from pygments.util import ClassNotFound

register = template.Library()

# Don't use this in the future, just include pykss is okay

@register.filter(name='highlight_code')
def highlight_code(code, lang):
    if code is not None:
        try:
            lexer = get_lexer_by_name(lang, encoding='utf-8', stripall=True, startinline=True)
        except ClassNotFound:
            lexer = get_lexer_by_name('text')
        formatter = HtmlFormatter(encoding='utf-8', style='colorful', cssclass='highlight',
                                  lineanchors="line")
        return highlight(code, lexer, formatter)
    else:
        return code
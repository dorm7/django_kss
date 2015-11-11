# Create your views here.
from django_kss.view_sets import StyleGuideViewSet


class StyleViewSet(StyleGuideViewSet):
    include_path = ['/Users/tim/Projects/django_kss/django_kss/sample/static/css/']
    exclude_pattern = 'vendor'
    style_names = ['css/form.css']

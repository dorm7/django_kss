# Create your views here.
from django_kss.view_sets import BaseStyleGuideViewSet


class StyleViewSet(BaseStyleGuideViewSet):
    include_path = ['/Users/tim/Projects/django_kss/django_kss_project/sample/static/css/']
    exclude_pattern = 'vendor'
    style_name = 'css/form.css'

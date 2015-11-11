from django.conf.urls import patterns, include, url
from .views import AutoStyleGuideView
from . import utils

def make_style_guide_pattern(template_name='styleguide.html'):
    view = AutoStyleGuideView.as_view(template_name=template_name)
    return patterns(
        '',
        url(r'^$', view, name='styleguide'),
        url(r'^(?P<app_name>.*)/(?P<section>.*)/$', view, name='styleguide'),
        url(r'^(?P<app_name>.*)/$', view, name='styleguide'),
        )

urlpatterns = make_style_guide_pattern()

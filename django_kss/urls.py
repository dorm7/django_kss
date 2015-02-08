from django.conf.urls import patterns, include, url
from .views import AutoStyleGuideView, render_prototype
from . import utils

def make_style_guide_pattern(template_name='styleguide.html'):
    view = AutoStyleGuideView.as_view(template_name=template_name)
    return patterns(
        '',
        url(r'^(?P<html>.*\.html)$', render_prototype, name='prototype'),
        url(r'^$', view, name='styleguide'),
        url(r'^(?P<app_name>.*)/$', view, name='styleguide'),
        url(r'^(?P<app_name>.*)/(?P<section>\d*)$', view, name='styleguide'),
        )

urlpatterns = make_style_guide_pattern()

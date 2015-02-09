from django.conf.urls import patterns, include, url
from .views import AutoStyleGuideView, FullTemplateStyleGuideView, InlineTemplateStyleGuideView
from . import utils

def make_style_guide_pattern(template_name='styleguide.html'):
    view = AutoStyleGuideView.as_view(template_name=template_name)
    return patterns(
        '',
        url(r'^$', view, name='styleguide'),
        url(r'^full/(?P<app_name>.*)/(?P<html>.*\.html)$', FullTemplateStyleGuideView.as_view(), name='prototype'),
        url(r'^(?P<app_name>.*)/(?P<html>.*\.html)/$', InlineTemplateStyleGuideView.as_view(), name='inline_prototype'),
        url(r'^(?P<app_name>.*)/(?P<section>.*)/$', view, name='styleguide'),
        url(r'^(?P<app_name>.*)/$', view, name='styleguide'),
        )

urlpatterns = make_style_guide_pattern()

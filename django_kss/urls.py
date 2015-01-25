from django.conf.urls import patterns, include, url
from .views import AutoStyleGuideView, render_prototype


def make_style_guide_pattern( template_name='styleguide.html' ):
	return patterns(
		'',
		url(r'^(?P<html>.*\.html)$', render_prototype),
		url(
			r'^(?P<section>\d*)$',
			AutoStyleGuideView.as_view(template_name=template_name),
			name='styleguide',
		),
	)
	
urlpatterns = make_style_guide_pattern()

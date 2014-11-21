from django.conf.urls import patterns, include, url
from .views import AutoStyleGuideView


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'django_kss_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(
        r'^(?P<section>\d*)$',
        AutoStyleGuideView.as_view(template_name='styleguide.html'),
        name='styleguide',
    ),
)

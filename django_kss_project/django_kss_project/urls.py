from django.conf.urls import patterns, include, url
from django.contrib import admin
import django_kss.urls
from sample.views import StyleViewSet
admin.autodiscover()



urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'django_kss_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^guide/', include(StyleViewSet.urls())),
)

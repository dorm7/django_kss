from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_kss.view_sets import StyleGuideViewSet
admin.autodiscover()


urlpatterns = [
    url(r'', include(StyleGuideViewSet.urls())),
    url(r'^admin/', include(admin.site.urls)),
]

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_kss.view_sets import StyleGuideViewSet
from pathlib import Path

admin.autodiscover()


class MyViewSet(StyleGuideViewSet):
    style_names = []


    exclude_pattern = None
    include_path = [str(Path.cwd().parent/'django_kss'/'static'/'django_kss'/'css')]  # Default to Project Static Path

urlpatterns = [
    url(r'', include(StyleGuideViewSet.urls())),
    url(r'^admin/', include(admin.site.urls)),
]

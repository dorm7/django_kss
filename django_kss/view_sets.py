from django.conf.urls import url
from django_kss.views import StyleGuideView
from pathlib import Path


class StyleGuideViewSet(object):

    style_names = map(lambda name: 'django_kss/css/' + name, ['device-list.css', 'icons.css', 'layout.css'])  # Auto Detect suffix, Default to all.scss
    exclude_pattern = None
    include_path = [str(Path.cwd().parent/'django_kss'/'static'/'django_kss'/'css')]  # Default to Project Static Path

    @classmethod
    def urls(cls):

        view = StyleGuideView.as_view(style_names=cls.style_names,
                                      exclude_pattern=cls.exclude_pattern,
                                      include_path=cls.include_path)
        return [
            url(r'^$', view, name='styleguide'),
            url(r'^/(?P<filename>.*)/$', view, name='styleguide'),
        ]

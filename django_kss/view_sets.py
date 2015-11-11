from django.conf.urls import url
from django_kss.views import AutoStyleGuideView


class BaseStyleGuideViewSet(object):

    style_name = None  # Auto Detect suffix, Default to all.scss
    exclude_pattern = None  # Default exclude vendor
    include_path = []  # Default to Project Static Path

    @classmethod
    def urls(cls):
        """
        :return: urlpatterns
        """

        view = AutoStyleGuideView.as_view(style_name=cls.style_name,
                                          exclude_pattern=cls.exclude_pattern,
                                          include_path=cls.include_path)
        return [
            url(r'^$', view, name='styleguide'),
            url(r'^/(?P<filename>.*)/$', view, name='styleguide'),
        ]

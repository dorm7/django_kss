import os.path
from pygments.formatters import HtmlFormatter
from django.utils.functional import cached_property

from django import conf
from django.views.generic.base import TemplateView
from django.shortcuts import render


from . import utils
from . import pykss


def render_prototype(request, html):
    prototype_directory = dirs = getattr(conf.settings, 'PROTOTYPR_DIR', "prototype")
    return render(request, os.path.join(prototype_directory, html))


class StyleguideMixin(object):
    def get_styleguide(self):
        dirs = getattr(conf.settings, 'PYKSS_DIRS', [])
        return pykss.Parser(*dirs)

    def get_context_data(self, **kwargs):
        context = super(StyleguideMixin, self).get_context_data(**kwargs)
        context.update({'styleguide': self.get_styleguide()})
        return context


class StyleguideView(StyleguideMixin, TemplateView):
    pass


class AutoStyleGuideView(TemplateView):

    def styleguide_settings(self, settings):
        return settings.items()

    def _get_settings(self):
        return utils.get_styleguide()

    def _get_setting(self, settings):
        try:
            app_name = self.kwargs['app_name']
            return settings[app_name]
        except KeyError:
            return settings.values()[0]

    def get_styleguide(self, settings):
        setting = self._get_setting(settings)
        return pykss.Parser(setting['source_dir'])

    def css_source_files(self, settings):
        return self._get_setting(settings)['target_files']

    @cached_property
    def pygament_style(self):
        return HtmlFormatter().get_style_defs('.highlight')

    def get_context_data(self, **kwargs):

        context = super(AutoStyleGuideView, self).get_context_data(**kwargs)

        settings = self._get_settings()
        context.update({'styleguide': self.get_styleguide(settings)})
        context.update({'styleguide_settings': self.styleguide_settings(settings)})
        context.update({'css_source_files': self.css_source_files(settings)})

        styleguide = context["styleguide"]

        def section_main_key(tp):
            key = tp[0]
            return key.split(".")[0]

        sections = list(
            sorted(
                set(
                    map(
                        lambda key: key.split(".")[0],
                        styleguide.sections
                    )
                )
            )
        )

        if 'section' not in self.kwargs or not self.kwargs['section']:
            current_section = sections[0]
        else:
            current_section = self.kwargs['section']

        section_descriptions = {}
        for section in sections:
            if section in styleguide.sections:
                section_descriptions[section] = \
                    styleguide.sections[section].description
            else:
                section_descriptions[section] = section

        context.update({'app_name': self._get_setting(settings)['app_name']})
        context.update({'current_section': current_section})
        context.update({'section_descriptions': section_descriptions})
        return context

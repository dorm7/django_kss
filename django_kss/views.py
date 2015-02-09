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
    return render(request, "styleguide-full-content.html",
                  { 'inline_content': os.path.join(prototype_directory, html)})


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
        return map(lambda fn: [fn, fn.endswith('scss')], self._get_setting(settings)['target_files'])

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
        file_names = set(map(lambda section: section.filename, styleguide.sections.values()))

        if 'section' not in self.kwargs or not self.kwargs['section']:
            current_section = styleguide.sections.values()[0].section
        else:
            target_filename = self.kwargs['section']
            possible = filter(lambda section: section.filename == target_filename, styleguide.sections.values())
            current_section = possible[0].section
        current_section_prefix = current_section.split(".")[0]

        context.update({'app_name': self._get_setting(settings)['app_name']})
        context.update({'current_section': current_section_prefix})
        context.update({'file_names': file_names})
        context.update({'htmls': self._get_setting(settings)['htmls']})
        return context


class InlineTemplateStyleGuideView(AutoStyleGuideView):

    template_name = 'styleguide-inline-content.html'

    def get_context_data(self, **kwargs):
        context = super(InlineTemplateStyleGuideView, self).get_context_data(**kwargs)
        context.update({'inline_content': 'prototype/' + self.kwargs['html']})
        context.update({'html': self.kwargs['html']})
        return context

class FullTemplateStyleGuideView(AutoStyleGuideView):

    template_name = 'styleguide-full-content.html'

    def get_context_data(self, **kwargs):
        context = super(FullTemplateStyleGuideView, self).get_context_data(**kwargs)
        context.update({'inline_content': 'prototype/' + self.kwargs['html']})
        return context

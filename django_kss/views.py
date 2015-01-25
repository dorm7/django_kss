import os.path
from pygments.formatters import HtmlFormatter
from django.utils.functional import cached_property

from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render


from . import pykss

def render_prototype(request, html):
	prototype_directory = dirs = getattr(settings, 'PROTOTYPR_DIR', "prototype")
	return render( os.path.join(prototype_directory, html))

class StyleguideMixin(object):

    def get_styleguide(self):
        dirs = getattr(settings, 'PYKSS_DIRS', [])
        return pykss.Parser(*dirs)

    def get_context_data(self, **kwargs):
        context = super(StyleguideMixin, self).get_context_data(**kwargs)
        context.update({'styleguide': self.get_styleguide()})
        return context


class StyleguideView(StyleguideMixin, TemplateView):
    pass


class AutoStyleGuideView(StyleguideView):

    @cached_property
    def css_source_files(self):
        return getattr(settings, "PYKSS_STATIC_FILES", [])

    @cached_property
    def pygament_style(self):
        return HtmlFormatter().get_style_defs('.highlight')

    def get_context_data(self, **kwargs):

        context = super(AutoStyleGuideView, self).get_context_data(**kwargs)
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

        if not self.kwargs['section']:
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

        context.update({'current_section': current_section})
        context.update({'section_descriptions': section_descriptions})
        return context

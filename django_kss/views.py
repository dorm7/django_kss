from pygments.formatters import HtmlFormatter
from django.conf import settings
from django.utils.functional import cached_property
from pykss.contrib.django.views import StyleguideView


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

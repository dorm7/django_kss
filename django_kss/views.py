from django.shortcuts import render
from django.conf import settings
from pykss.contrib.django.views import StyleguideView
import itertools


class AutoStyleguideView(StyleguideView):

    def get_context_data(self, **kwargs):

        context = super(AutoStyleguideView, self).get_context_data(**kwargs)
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

        section_descriptions = {}
        for section in sections:
            if section in styleguide.sections:
                section_descriptions[section] = \
                    styleguide.sections[section].description
            else:
                section_descriptions[section] = section

        context.update({'sections': sections})
        context.update({'section_descriptions': section_descriptions})
        context.update({'PYKSS_STATIC_FILES':
                        getattr(settings, "PYKSS_STATIC_FILES", [])
                        })
        return context

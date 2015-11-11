import logging
from django.views.generic.base import TemplateView
from pykss.style_guide_manager import StyleGuideManager


logger = logging.getLogger(__name__)


class StyleGuideView(TemplateView):

    style_names = []
    exclude_pattern = None
    include_path = []

    template_name = 'django_kss/styleguide.html'

    def domain(self):
        host = self.request.META['HTTP_HOST']
        domain = host.split(":")[0]
        return domain

    def _get_filename(self, filenames):

        if 'filename' in self.kwargs and self.kwargs['filename']:
            return self.kwargs['filename']
        else:
            return filenames[0]

    def get_context_data(self, **kwargs):

        print self.include_path
        logger.debug('include path', self.include_path)
        logger.debug('exclude pattern', self.exclude_pattern)

        styleguide_manager = StyleGuideManager(self.include_path, self.exclude_pattern)

        context = super(StyleGuideView, self).get_context_data(**kwargs)

        filenames = styleguide_manager.filenames()

        context.update({'css_source_files': filenames})
        context.update({'current_file': self._get_filename(filenames)})
        context.update({'current_sections': styleguide_manager.get_sections(self._get_filename(
            filenames
        ))})
        context.update({'styleguide': styleguide_manager.style_guide})

        return context



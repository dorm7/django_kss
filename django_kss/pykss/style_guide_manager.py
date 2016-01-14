from . import parser


class StyleGuideManager(object):
    def __init__(self, dirs=(), exclude_pattern="vendor"):
        self.style_guide = parser.Parser(*dirs, exclude_pattern=exclude_pattern)

    def filenames(self):
        return list(sorted(list(set(map(lambda section: section.filename, self.style_guide.sections.values())))))

    def get_sections(self, file_name):
        sections = filter(lambda section: section.filename == file_name, self.style_guide.sections.values())
        return sections



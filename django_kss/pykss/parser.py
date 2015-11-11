import logging
import os
import re
from .comment import CommentParser
from .exceptions import SectionDoesNotExist
from .section import Section

logger = logging.getLogger(__name__)

EXCLUDE_PATTERN_ARG = 'exclude_pattern'


class Parser(object):
    def __init__(self, *paths, **kwargs):
        logger.debug('constructed path is %s', paths)
        self.paths = paths
        self.pattern_checker = PatternChecker(kwargs.get(EXCLUDE_PATTERN_ARG, None))
        self._sections = self.parse()

    def parse(self):
        sections = {}

        filenames = [os.path.join(subpath, filename)
                     for path in self.paths
                     for subpath, dirs, files in os.walk(path)
                     for filename in files]

        filenames = filter(lambda file_name: not self.pattern_checker.in_pattern(file_name), filenames)
        logger.debug('filtered filenames %s', filenames)

        for filename in filenames:
            parser = CommentParser(filename)
            for block in parser.blocks:
                section = Section(block, os.path.basename(filename))
                if section.section:
                    sections[section.section] = section

        return sections

    @property
    def sections(self):
        return self._sections

    def section(self, reference):
        try:
            return self.sections[reference]
        except KeyError:
            raise SectionDoesNotExist('Section "%s" does not exist.' % reference)


class PatternChecker(object):

    def __init__(self, pattern=None):
        logger.debug("pattern is %s", pattern)
        if pattern:
            self.pattern = re.compile(pattern, re.IGNORECASE)
        else:
            self.pattern = None

    def in_pattern(self, string_data):
        if not self.pattern:
            return False
        return bool(self.pattern.search(string_data))

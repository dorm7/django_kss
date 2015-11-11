import pathlib
from nose.tools import eq_
from ..pykss import Parser
from .utils import TEST_DATA_PATH

# Create your tests here.

def section_correct_test():
    test_data_path = TEST_DATA_PATH
    parser = Parser(test_data_path)
    sections = parser.sections
    eq_(len(sections), 4)


def section_exclude_test():
    test_data_path = TEST_DATA_PATH
    parser = Parser(test_data_path, exclude_pattern='vendor')
    sections = parser.sections
    eq_(len(sections), 2)


from ..pykss.style_guide_manager import StyleGuideManager
from nose.tools import eq_
from utils import TEST_DATA_PATH


def file_name_listing_test():

    test_data_path = TEST_DATA_PATH

    filenames = StyleGuideManager([test_data_path], 'vendor').filenames()

    eq_(len(filenames), 1)


def section_listing_test():

    test_data_path = TEST_DATA_PATH

    guide = StyleGuideManager([test_data_path], 'vendor')
    sections = guide.get_sections('from.css')

    eq_(len(sections), 2)

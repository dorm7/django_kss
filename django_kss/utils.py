from __future__ import print_function
import imp
import logging
import os
import os.path
import sys
from importlib import import_module
from django.conf import settings


logger = logging.getLogger(__name__)


def _get_styleguide_module(module_name='styleguide'):

    style_guides = []
    modules_to_check = []

    # Hackish: do this in case we have some project top-level
    # (homepage, etc) urls defined project-level instead of app-level.
    settings_module = settings.SETTINGS_MODULE
    if settings_module:
        if "." in settings_module:
            # strip off '.settings" from end of module
            # (want project module, if possible)
            settings_module = settings_module.split(".", 1)[0]
        modules_to_check += [settings_module, ]

    # INSTALLED_APPS that aren't the project itself (also ignoring this
    # django_medusa module)
    modules_to_check += filter(
        lambda x: (x != "django_kss") and (x != settings_module),
        settings.INSTALLED_APPS
    )

    for app in modules_to_check:
        try:
            import_module(app)
            app_path = sys.modules[app].__path__
        except AttributeError:
            logger.debug("Skipping app '%s'... (Not found)", app)
            continue
        try:
            imp.find_module(module_name, app_path)
        except ImportError:
            logger.debug("Skipping app '%s'... (No 'styleguide.py')" , app)
            continue
        try:
            app_styleguide_module = import_module('%s.%s' % (app, module_name))
            if hasattr(app_styleguide_module, "styleguide"):
                style_guides.append(app_styleguide_module)
            else:
                logger.debug("Skipping app '%s'... ('%s.styleguide' does not contain "\
                      "'styleguide' var (list of styleguide classes)" , (app, app))
        except AttributeError:
            logger.debug("Skipping app '%s'... (Error importing '%s.styleguide')" , (
                app, app
            ))
            continue
        logger.debug("Found styleguide for '%s'..." , app)
    return style_guides


def _remove_static(target_file):
    if target_file.startswith('static/'):
        return target_file.replace('static/', '')
    return target_file


def _complete_setting(m):
    app_path = os.path.dirname(m.__file__)

    try:
        source_dir = m.styleguide['source_dir']
    except KeyError:
        source_dir = 'static/css'
    abs_source_dir = os.path.join(app_path, source_dir)
    print(source_dir)

    try:
        verbose_name = m.styleguide['verbose_name']
    except KeyError:
        verbose_name = m.__name__

    try:
        target_files = m.styleguide['target_files']
        if isinstance(target_files, str):
            target_files = [target_files]
    except KeyError:
        target_files = os.listdir(abs_source_dir)
        target_files = map(lambda x: os.path.join(source_dir, x), target_files)

    try:
        htmls = os.listdir(os.path.join(app_path, 'templates', 'prototype'))
    except OSError:
        htmls = []

    target_files = map(_remove_static, target_files)

    styleguide = m.styleguide.copy()
    styleguide['source_dir'] = abs_source_dir
    styleguide['app_name'] = m.__name__
    styleguide['verbose_name'] = verbose_name
    styleguide['target_files'] = target_files
    styleguide['htmls'] = htmls
    return styleguide


def get_styleguide():
    safe_settings = map(_complete_setting, _get_styleguide_module())
    setting_map = {}
    for setting in safe_settings:
        setting_map[setting['app_name']] = setting
    return setting_map



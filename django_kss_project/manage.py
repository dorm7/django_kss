#!/usr/bin/env python
import os
import sys

dirname = os.path.dirname(os.path.dirname( os.path.abspath( __file__)))
sys.path.append(
    dirname
)
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_kss_project.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

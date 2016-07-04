#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlinedbproject.settings")
    from django.core.handlers.wsgi import WSGIHandler
    from django.core.management import execute_from_command_line

    application = WSGIHandler()
    execute_from_command_line(sys.argv)

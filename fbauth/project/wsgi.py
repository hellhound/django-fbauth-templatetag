# -*- coding:utf-8 -*-
'''
WSGI config for fblogin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
'''
import os
import sys
import settings

sys.path.insert(0, os.path.join(settings.ROOT_DIR, 'apps'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

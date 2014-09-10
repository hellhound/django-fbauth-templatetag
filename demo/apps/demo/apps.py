# -*- coding:utf-8 -*-
from django.apps import AppConfig

from . import strings


class DemoConfig(AppConfig):
    name = 'demo'
    verbose_name = strings.DEMO_CONFIG_VERBOSE_NAME

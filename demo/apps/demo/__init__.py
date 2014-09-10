# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.conf import settings

setattr(settings, 'FBAUTH_REDIRECT_URL',
    reverse('demo:redirect') + '?access_token={0}')

default_app_config = 'demo.apps.DemoConfig'

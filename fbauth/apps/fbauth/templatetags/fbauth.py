# -*- coding:utf-8 -*-
from django import template
from django.template.loader import render_to_string
from django.conf import settings

from .. import constants

register = template.Library()


@register.inclusion_tag('fbauth/css.html')
def fbauth_css():
    return {}


@register.inclusion_tag('fbauth/button.html')
def fbauth_button():
    return dict(
        JQUERY_CDN=constants.JQUERY_CDN,
        JQUERY_REQUIRED_VERSION=constants.JQUERY_REQUIRED_VERSION,
        FACEBOOK_API=constants.FACEBOOK_API,
        FACEBOOK_APP_ID=constants.FACEBOOK_APP_ID,
        FBAUTH_REDIRECT_URL=unicode(
            getattr(settings, 'FBAUTH_REDIRECT_URL', '{0}')))

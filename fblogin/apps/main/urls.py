# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='main/main.html')),
    url(r'^channel.html$',
        TemplateView.as_view(template_name='main/channel.html')),
)

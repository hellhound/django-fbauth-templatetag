# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='demo/demo.html')),
    url(r'^redirect/$',
        TemplateView.as_view(template_name='demo/redirect.html'),
    name='redirect'),
)

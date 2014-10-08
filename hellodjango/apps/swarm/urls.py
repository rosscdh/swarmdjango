# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='swarm/welcome.html'), name='welcome'),
)

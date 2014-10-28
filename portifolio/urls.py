# -*- coding: utf-8 -*-
#
#  portifolio/urls.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as urls da aplicação django de portifolio
#

from django.conf.urls import patterns, include, url

urlpatterns = patterns('portifolio.views',
    url(r'^$', 'portifolio_index', name='portifolio_index'),
    url(r'^(?P<slug>[\w_-]+)/$', 'portifolio_item',name='portifolio_item'),    
)
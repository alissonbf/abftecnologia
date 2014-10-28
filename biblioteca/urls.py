# -*- coding: utf-8 -*-
"""
Arquivo de configuração das urls da aplicação biblioteca

Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
"""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('biblioteca.views',
    url(r'^$', 'biblioteca_index', name='biblioteca_index'),
    url(r'^(?P<slug>[\w_-]+)/$', 'biblioteca_artigo',name='biblioteca_artigo'),    
)
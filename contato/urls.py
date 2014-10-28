# -*- coding: utf-8 -*-
#
#  contato/urls.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as urls da aplicação django de contato
#

from django.conf.urls import patterns, include, url

urlpatterns = patterns('contato.views',
    url(r'^$', 'contato_index', name='contato_index'),
    url(r'^mensagem-enviada', 'contato_sucesso', name='contato_sucesso'),    
)
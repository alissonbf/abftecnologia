# -*- coding: utf-8 -*-
#
#  cliente/urls.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as urls da aplicação django de cliente
#

from django.conf.urls import patterns, include, url

urlpatterns = patterns('cliente.views',
    url(r'^$', 'cliente_index', name='cliente_index'),
    url(r'^sair', 'cliente_sair', name='cliente_sair'),
    url(r'^meu-perfil', 'cliente_perfil', name='cliente_perfil'),
    url(r'^meus-comentarios', 'cliente_comentarios', name='cliente_comentarios'),    
    url(r'^cadastro-realizado', 'cliente_sucesso', name='cliente_sucesso'),    
)
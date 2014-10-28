# -*- coding: utf-8 -*-
#
#  home/urls.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as urls da aplicação django de home

from django.conf.urls import patterns, include, url

urlpatterns = patterns('home.views',
    url(r'^$', 'home_index', name='home_index'),    
)
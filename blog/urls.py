# -*- coding: utf-8 -*-
#
#  blog/urls.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as urls da aplicação django de blog
#

from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'blog_index', name='blog_index'),
    url(r'^(?P<slug>[\w_-]+)/$', 'blog_post',name='blog_post'),
    url(r'^categoria/(?P<slug>[\w_-]+)/$', 'blog_categoria',name='blog_categoria'),
    url(r'^autor/(?P<slug>[\w_-]+)/$', 'blog_autor',name='blog_autor'),
    url(r'^tag/(?P<slug>[\w_-]+)/$', 'blog_tag',name='blog_tag'),
    
)
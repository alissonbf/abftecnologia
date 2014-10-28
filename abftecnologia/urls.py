# -*- coding: utf-8 -*-
#
#  abftecnologia/urls.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração das urls projeto django, abftecnologia

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

from sitemap import *

sitemaps = {
    'site':Sitemap(['home_index','portifolio_index','blog_index','contato_index',]),    
    'potifolio':PortifolioSitemap(['portifolio_index',]),    
    'blog':BlogSitemap(['blog_index']),
}

urlpatterns = patterns('',
    # Examples:    
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
        
    url(r'^$', include('home.urls')),
    
    url(r'^portifolio/', include('portifolio.urls')),
    url(r'^biblioteca/', include('biblioteca.urls')),        
    url(r'^contato/', include('contato.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^minha-area/', include('cliente.urls')),        
    
    url(r'', include('social_auth.urls')),
    
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

if settings.LOCAL:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
    
urlpatterns += staticfiles_urlpatterns()
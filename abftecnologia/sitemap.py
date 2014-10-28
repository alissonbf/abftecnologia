# -*- coding: utf-8 -*-
#
#  abftecnologia/sitemap.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração do sitemap do projeto django, abftecnologia

from django.contrib.sitemaps    import Sitemap
from django.core.urlresolvers   import reverse

from portifolio.models  import Item
from blog.models        import Post

import datetime

class Sitemap(Sitemap):
    def __init__(self, names):
        self.names      = names
        self.priority   = 0.5
        
    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'monthly'

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse(obj)
    
# portifolio
class PortifolioSitemap(Sitemap):
    changefreq  = "weekly"
    priority    = 0.5

    def items(self):
        return Item.objects.all().order_by('titulo')

    def lastmod(self, obj):
        return obj.created_on

    def location(self, obj):
        return obj.get_absolute_url()    

# blog
class BlogSitemap(Sitemap):
    changefreq  = "weekly"
    priority    = 0.5

    def items(self):
        return Post.objects.all().order_by('titulo')

    def lastmod(self, obj):
        return obj.created_on

    def location(self, obj):
        return obj.get_absolute_url()

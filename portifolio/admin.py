# -*- coding: utf-8 -*-
#
#  portifolio/admin.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração do admin do projeto django, portifolio

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from image_cropping import ImageCroppingMixin
from django.conf import settings

from models import Item, Categoria

class AdminItem(ImageCroppingMixin, ModelAdmin):
    class Media:
        js = (settings.STATIC_URL+'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', settings.STATIC_URL+'grappelli/tinymce_setup/tinymce_setup.js')
     
    list_display = ('titulo','created_on')        
    search_fields = ('titulo','texto')
    
admin.site.register(Item, AdminItem)
admin.site.register(Categoria)
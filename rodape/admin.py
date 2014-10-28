# -*- coding: utf-8 -*-
#
#  rodape/admin.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem a integração da aplicação django de rodape com o admin do django

from django.contrib                 import admin
from django.contrib.admin.options   import ModelAdmin

from django.forms   import TextInput
from django.db      import models

from models import Informacao, RedeSocial

class AdminInformacao(ModelAdmin):
    list_display = ('titulo','texto')

class AdminRedeSocial(ModelAdmin):
    list_display = ('titulo','link','icone')
    
admin.site.register(Informacao, AdminInformacao)
admin.site.register(RedeSocial, AdminRedeSocial)
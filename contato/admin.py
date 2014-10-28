# -*- coding: utf-8 -*-
#
#  contato/admin.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem a integração da aplicação django de contato com o admin do django

from django.contrib                 import admin
from django.contrib.admin.options   import ModelAdmin

from django.forms   import TextInput
from django.db      import models

from models import Contato, Telefone, Site, Email, Mensagem, GrupoNewsletter, Newsletter

class TelefoneInline(admin.TabularInline):
    model   = Telefone

class SiteInline(admin.TabularInline):
    model   = Site
    
    
class EmailInline(admin.TabularInline):
    model   = Email


class AdminContato(ModelAdmin):            
    inlines = [
        TelefoneInline,
        EmailInline,
        SiteInline
    ]

class AdminMensagem(ModelAdmin):
    readonly_fields = ('nome','email','site','mensagem',)
    list_display    = ('nome','email','site','mensagem',)
    list_filter     = ('created_on',)
    search_fields   = ('nome','email','mensagem','created_on',)

class AdminNewsletter(ModelAdmin):
    list_display    = ('assunto','grupo','mensagem','created_on',)
    list_filter     = ('created_on',)
    search_fields   = ('assunto','grupo',)

    
admin.site.register(Contato, AdminContato)
admin.site.register(Mensagem, AdminMensagem)
admin.site.register(Newsletter,AdminNewsletter)
admin.site.register(GrupoNewsletter)
    
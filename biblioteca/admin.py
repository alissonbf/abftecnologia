# -*- coding: utf-8 -*-
"""
Arquivo de configurações da administração para a aplicação biblioteca

Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
"""

from django.contrib import admin
from models         import Categoria, Artigo, Assinante


class AdminArtigo(admin.ModelAdmin):
    """ Configuração da exibição, busca e filtragem dos artigos da biblioteca """
    
    list_display    = ('titulo','categoria','created_on',)
    list_filter     = ('categoria',)
    search_fields   = ('titulo',)

class AdminAssinante(admin.ModelAdmin):
    """ Configuração da exibição, busca e filtragem dos assinantes dos artigos """
    
    list_display    = ('nome','email','empresa','site','artigo','created_on',)
    list_filter     = ('artigo','created_on',)
    search_fields   = ('nome','empresa',)

admin.site.register(Categoria)
admin.site.register(Artigo,AdminArtigo)
admin.site.register(Assinante,AdminAssinante)
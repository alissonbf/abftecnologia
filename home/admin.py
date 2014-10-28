# -*- coding: utf-8 -*-
#
#  home/admin.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração do admin do projeto django, home

from django.db                      import models
from django.contrib                 import admin


from models         import Slide, Servico, Vantagem, Trabalho


class AdminSlide(admin.ModelAdmin):     
    list_display    = ('titulo','subtitulo','ativo',)        
    search_fields   = ('titulo','subtitulo')

class AdminServico(admin.ModelAdmin):     
    list_display    = ('titulo','texto','icone')            
    search_fields   = ('titulo','texto')

class AdminVantagem(admin.ModelAdmin):     
    list_display    = ('titulo','texto','icone')            
    search_fields   = ('titulo','texto')

class AdminTrabalho(admin.ModelAdmin):     
    list_display    = ('titulo','texto','icone')            
    search_fields   = ('titulo','texto')
  
  
admin.site.register(Slide, AdminSlide)
admin.site.register(Servico, AdminServico)
admin.site.register(Vantagem, AdminVantagem)
admin.site.register(Trabalho, AdminTrabalho)
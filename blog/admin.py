# -*- coding: utf-8 -*-
#
#  blog/admin.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração do admin do projeto django, blog

from django.db                      import models
from django.conf                    import settings
from django.forms                   import TextInput
from django.contrib                 import admin
from django.contrib.admin.options   import ModelAdmin

from image_cropping     import ImageCroppingMixin
from models             import Post, Categoria, Comentario, Audio, Apresentacao, Video


class AudioInline(admin.TabularInline):
    """ Formulario inline da playlist """
    model   = Audio
    max_num = 1

class ApresentacaoInline(admin.TabularInline):
    """ Formulario inline da apresentação """
    model   = Apresentacao
    max_num = 1
    
class VideoInline(admin.TabularInline):
    """ Formulario inline do video """
    model   = Video
    max_num = 1
    
class AdminPost(ImageCroppingMixin, ModelAdmin):
    class Media:
        js = (settings.STATIC_URL+'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', settings.STATIC_URL+'grappelli/tinymce_setup/tinymce_setup.js')
        
    list_display    = ('titulo','get_user_firstname','categoria','created_on',)
    list_filter     = ('created_on',)
    search_fields   = ('titulo','texto',)

    inlines = [
        AudioInline,
        ApresentacaoInline,
        VideoInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        obj.save()
        
    def get_queryset(self, request):
        qs = super(AdminPost, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)    

class AdminComentario(ModelAdmin):
    list_display    = ('texto','status','get_user_firstname','post',)
    list_filter     = ('status','usuario')
    actions         = ['desbloquear_comentario','bloquear_comentario']
    
    def desbloquear_comentario(self, request, queryset):
        for obj in queryset:
            obj.status = u'desbloqueado'
            obj.save()
                        
    desbloquear_comentario.short_description = 'Desbloquear Comentário'

    def bloquear_comentario(self, request, queryset):
        for obj in queryset:
            obj.status = u'bloqueado'
            obj.save()
                        
    bloquear_comentario.short_description = 'Bloquear Comentário'
    
admin.site.register(Post, AdminPost)
admin.site.register(Categoria)
admin.site.register(Comentario, AdminComentario)
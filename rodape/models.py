# -*- coding: utf-8 -*-
#
#  rodape/models.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração dos modelos projeto django, rodape

from django.db              import models

from utils.audit            import AuditModel
from utils.singleton        import SingletonModel

class Informacao(SingletonModel):
    """  Informações do rodape """
    class Meta:        
        verbose_name = u'Informacao'
        verbose_name_plural = u'Informacao'

    titulo     = models.CharField(u'Titulo', max_length=30)
    logo       = models.ImageField(u'Logo',null=False,blank=False,upload_to='rodape/logo',help_text=u'Escolha uma imagem de 123x23')
    texto      = models.TextField(u'Texto', max_length=250)
    
    def __unicode__(self):
        return self.titulo

ICONE_CHOICES = (
    ('fui-facebook',    'Facebook'),
    ('fui-youtube',     'Youtube'),
    ('fui-vimeo',       'Vimeo'),
    ('fui-twitter',     'Twitter'),
    ('fui-pinterest,',  'Pinterest'),
    ('fui-myspace',     'MySpace'),
    ('fui-linkedin',    'Linkedin'),
    ('fui-googleplus',  'GooglePlus'),    
)

    
class RedeSocial(AuditModel):
    """  Rede Social da empresa """
    class Meta:        
        verbose_name = u'Rede Social'
        verbose_name_plural = u'Redes Sociais'

    titulo     = models.CharField(u'Titulo', max_length=30)
    link       = models.CharField(u'Link', max_length=100, default=u'http://')
    icone      = models.CharField(u'Icone', max_length=100, choices=ICONE_CHOICES)
    
    def __unicode__(self):
        return self.titulo
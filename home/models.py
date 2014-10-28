# -*- coding: utf-8 -*-
#
#  home/models.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração dos modelos projeto django, home

from django.db              import models

from utils.audit            import AuditModel

class Slide(AuditModel):
    """  Slide do slideshow """
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Slide'
        verbose_name_plural = u'Slides'
        
    titulo      = models.CharField(u'Titulo', max_length=45)
    subtitulo   = models.CharField(u'Subtitulo', max_length=46)
    link        = models.CharField(u'Link', max_length=200,default=u'http://')
    imagem      = models.ImageField(null=False, blank=False, upload_to='slide/imagem',help_text=u'Escolha imagens de 1000x750')    
    ativo       = models.BooleanField(u'Slide Ativo',default=True, help_text=u'Apenas slides ativos aparecem na home.')
    
    def __unicode__(self):
        return self.titulo

ICONE_CHOICES = (
    ('fa-rocket',       'Foguete'),
    ('fa-magic',        'Varinha Mágica'),
    ('fa-briefcase',    'Maleta'),
    ('fa-cogs',         'Engrenagem'),
    ('fa-leaf',         'Folha de árvore'),
    ('fa-plane',        'Avião'),
    ('fa-comments',     'Balão de Fala'),
      
    ('fa-bell',         'Sino'),
    ('fa-thumbs-up',    'Joinha'),
    ('fa-camera',       'Maquina Fotográfica'),
    ('fa-flask',        'Tubo de ensaio'),
    ('fa-heart',        'Coração'),
    ('fa-gift',         'Presente'),
    
    ('fa-glass',        'Taça'),
    ('fa-music',        'Nota Musical'),
    ('fa-search',       'Lupa'),
    ('fa-envelope',     'Envelope'),    
    ('fa-star',         'Estrela'),
)    

ORDEM_CHOICES = (('1','1º'),('2','2º'),('3','3º'),('4','4º'),('5','5º'),('6','6º'))

class Servico(AuditModel):
    """  Serviços prestados pela empresa """
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Serviço'
        verbose_name_plural = u'Serviços'
        
    titulo      = models.CharField(u'Titulo', max_length=30)
    texto       = models.TextField(u'Texto', max_length=150)
    icone       = models.CharField(u'Icone', max_length=100, choices=ICONE_CHOICES)

    def __unicode__(self):
        return self.titulo  

    
class Vantagem(AuditModel):
    """  Vantagem de contratar a empresa """
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Vantagem'
        verbose_name_plural = u'Vantagens'
        
    titulo      = models.CharField(u'Titulo', max_length=80)
    texto       = models.TextField(u'Texto', max_length=250)
    icone       = models.CharField(u'Icone', max_length=100, choices=ICONE_CHOICES)

    def __unicode__(self):
        return self.titulo
    
class Trabalho(AuditModel):
    """  Vantagem de contratar a empresa """
    class Meta:
        ordering = ['ordem',]
        verbose_name = u'Trabalho'
        verbose_name_plural = u'Trabalhos'
        
    titulo      = models.CharField(u'Titulo', max_length=30)
    texto       = models.TextField(u'Texto', max_length=60)
    icone       = models.CharField(u'Icone', max_length=100, choices=ICONE_CHOICES)
    ordem       = models.CharField(u'Ordem',max_length=10,choices=ORDEM_CHOICES)
    
    def __unicode__(self):
        return self.titulo    
# -*- coding: utf-8 -*-
"""
Arquivo de modelos da aplicação biblioteca

Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
"""

from django.db      import models

from django.core.urlresolvers       import reverse

from utils.audit    import AuditModel

class Categoria(AuditModel):
    """  Categoria dos artigos da biblioteca """
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    titulo      = models.CharField(u'Titulo', max_length=100)    
    slug        = models.SlugField(u'Link', max_length=100, blank=True, unique=True,help_text=u'Deixe em branco para preenchimento automatico.')

    def __unicode__(self):
        return self.titulo

class Artigo(AuditModel):
    """  E-books, infograficos e etc disponiveis na biblioteca """
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Artigo'
        verbose_name_plural = u'Artigos'

    titulo      = models.CharField(u'Titulo', max_length=100)
    descricao   = models.TextField(u'Descrição', null=True,blank=False,help_text=u'Descrição sobre oque é o artigo, aparecerá na meta-description e caso não tenha nada no campo código.')
    imagem      = models.ImageField(null=False, blank=False, upload_to='biblioteca/miniatura',help_text=u'Escolha uma imagem de 303x202')
    codigo      = models.TextField(u'Código', null=True,blank=True,help_text=u'Código de incorporação da apresentação.')
    arquivo     = models.FileField(u'Arquivo',null=False, blank=False, upload_to='biblioteca/arquivo',help_text=u'Arquivo que será feito download.')    
    categoria	= models.ForeignKey(Categoria,verbose_name=u'Categoria')
    slug        = models.SlugField(u'Link', max_length=100, blank=True, unique=True,help_text=u'Deixe em branco para preenchimento automatico.')

    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('biblioteca_artigo', kwargs={'slug': self.slug})


class Assinante(AuditModel):
    """  Assinante dos artigos da biblioteca """
    class Meta:
        ordering = ['nome',]
        verbose_name = u'Assinante'
        verbose_name_plural = u'Assinantes'

    nome        = models.CharField(u'Nome', max_length=200, blank=True,null=True)    
    email       = models.EmailField(u'Email', max_length=200, blank=True,null=True)
    empresa     = models.CharField(u'Empresa', max_length=200, blank=True,null=True)
    site        = models.CharField(u'Site', max_length=200, blank=True,null=True)    
    artigo	= models.ForeignKey(Artigo,verbose_name=u'Artigo')
    
    def __unicode__(self):
        return self.nome

#SIGNAL
from django.db.models       import signals
from utils.signals_comuns   import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Categoria)
signals.pre_save.connect(slug_pre_save, sender=Artigo)
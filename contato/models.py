# -*- coding: utf-8 -*-
#
#  contato/models.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração dos modelos projeto django, contato

from django.db              import models

from django.contrib.auth.models import User

from utils.audit            import AuditModel
from utils.singleton        import SingletonModel

from blog.models            import Post
from portifolio.models      import Item

class Contato(SingletonModel):
    """  Informações da pagina de contato """
    class Meta:        
        verbose_name = u'Contato'
        verbose_name_plural = u'Contato'

    endereco    = models.CharField(u'Endereço', max_length=300)
    codigo      = models.TextField(u'Mapa', help_text=u'Codigo do gmaps')
    
    def __unicode__(self):
        return u'Pagina de Contato'
    
class Telefone(AuditModel):
    """  Telefones de contato da empresa """    
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Telefone'
        verbose_name_plural = u'Telefones'
        
    contato 	= models.ForeignKey('Contato',related_name='telefones')
    titulo      = models.CharField(u'Titulo', max_length=100)
    telefone    = models.CharField(u'Telefone', max_length=100)    

    def __unicode__(self):
        return self.titulo
    
class Site(AuditModel):
    """  Sites de contato da empresa """    
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Site'
        verbose_name_plural = u'Sites'
        
    contato 	= models.ForeignKey('Contato',related_name='sites')
    titulo      = models.CharField(u'Titulo', max_length=100)
    site        = models.CharField(u'Site', max_length=100)    

    def __unicode__(self):
        return self.titulo

class Email(AuditModel):
    """  Emails de contato da empresa """    
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Email'
        verbose_name_plural = u'Emails'
        
    contato 	= models.ForeignKey('Contato',related_name='emails')
    titulo      = models.CharField(u'Titulo', max_length=100)
    email       = models.EmailField(u'Email', max_length=100)    

    def __unicode__(self):
        return self.titulo
    
class Mensagem(AuditModel):
    """  Mensagem de contato enviada para a empresa """    
    class Meta:
        ordering = ['created_on',]
        verbose_name = u'Mensagem'
        verbose_name_plural = u'Mensagens'
            
    nome        = models.CharField(u'Nome', max_length=100)
    email       = models.EmailField(u'Email', max_length=100)
    site        = models.CharField(u'Site', max_length=100)
    mensagem    = models.TextField(u'Mensagem')

    def __unicode__(self):
        return self.nome
    
    
class GrupoNewsletter(AuditModel):
    """ Grupo de usuarios que reseberão a newsletter """
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Grupo Newsletter'
        verbose_name_plural = u'Grupos Newsletter'
        
    titulo        = models.CharField(u'Titulo', max_length=100,null=True,blank=False)
    destinatario  = models.ManyToManyField(User,u'Destinatários',related_name='destinatario',null=False,blank=False)
    
    def __unicode__(self):
        return self.titulo
    
class Newsletter(AuditModel):
    """ Mensagem com atualizações do site """
    class Meta:
        ordering = ['assunto',]
        verbose_name = u'Newsletter'
        verbose_name_plural = u'Newsletters'
        
    nome                = models.CharField(u'Nome', help_text=u'Nome da empresa',max_length=100,null=True,blank=False)
    assunto             = models.CharField(u'Assunto', max_length=100,null=True,blank=False)
    mensagem            = models.TextField(u'Mensagem',null=True,blank=False)
    grupo 	        = models.ForeignKey(GrupoNewsletter,related_name='destinatarios',null=False,blank=False)
    portifolio_item_1   = models.ForeignKey(Item,related_name='portifolio_item_1',null=True,blank=True)
    portifolio_item_2   = models.ForeignKey(Item,related_name='portifolio_item_2',null=True,blank=True)
    portifolio_item_3   = models.ForeignKey(Item,related_name='portifolio_item_3',null=True,blank=True)    
    blog_post           = models.ManyToManyField(Post,related_name='blog_post',null=False,blank=False)
    
    def __unicode__(self):
        return self.assunto
    
#SIGNAL
from django.db.models      import signals
from signals_contato       import enviar_newsletter

signals.post_save.connect(enviar_newsletter, sender=Newsletter)
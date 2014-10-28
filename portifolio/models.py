# -*- coding: utf-8 -*-
#
#  portifolio/models.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração dos modelos projeto django, portifolio

from django.db                  import models
from django.core.urlresolvers   import reverse

from image_cropping         import ImageRatioField
from utils.audit            import AuditModel
from utils.singleton        import SingletonModel

class Categoria(AuditModel):
    """  Categoria dos itens do portifolio """
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    titulo      = models.CharField(u'Titulo', max_length=100)    

    def __unicode__(self):
        return self.titulo

class Item(AuditModel):
    """  Item de um portifolio """
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Item'
        verbose_name_plural = u'Itens'
        
    titulo      = models.CharField(u'Titulo', max_length=100)
    texto       = models.TextField(u'Texto')
    miniatura   = models.ImageField(null=False, blank=False, upload_to='portifolio/miniatura',help_text=u'Escolha imagens entre 303x202 e 800x500')
    cropping    = ImageRatioField('miniatura', '303x202')    
    categoria	= models.ForeignKey(Categoria,verbose_name=u'Categoria')
    slug        = models.SlugField(u'Link', max_length=100, blank=True, unique=True,help_text=u'Deixe em branco para preenchimento automatico.')
        
    
    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('portifolio_item', kwargs={'slug': self.slug})
    
#SIGNAL
from django.db.models import signals
from utils.signals_comuns import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Item)
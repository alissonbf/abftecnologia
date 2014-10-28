# -*- coding: utf-8 -*-
"""
Arquivo de classes abstratas de imagens

Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
"""

from django.db          import models
from image_cropping 	import ImageRatioField

class GaleriaAbstract(models.Model):
    """
        Modelo de imagem para ser usada em galerias.
        
        Como usar:
        from multimidia.imagem import GaleriaAbstract
        
        class Imagem(GaleriaAbstract):
            historia 	= models.ForeignKey('Historia',related_name='galeria', blank=True, null=True)
    """
    # Image fields    
    titulo 	= models.CharField(verbose_name=u'Titulo', max_length=200, help_text=u'O nome da imagem')	
    original 	= models.ImageField(null=False,blank=False,upload_to='multimidia/galeria', help_text=u'Escolha imagens de 800x600')    
    cropping    = ImageRatioField('original', '430x325')
    
    # Audit fields                                                              
    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    class Meta:
        abstract = True
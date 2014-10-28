# -*- coding: utf-8 -*-
"""
Arquivo de classes abstratas de video

Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
"""

from django.db          import models

class VideoAbstract(models.Model):
    """
        Modelo de video para ser usada em galerias de video.
        
        Como usar:
        from multimidia.video import VideoAbstract
        
        class Video(VideoAbstract):
            historia 	= models.ForeignKey('Historia',related_name='galeria', blank=True, null=True)
    """
    # Image fields    
    titulo  = models.CharField(verbose_name=u'Titulo', max_length=200,blank=True,null=True, help_text=u'O nome do video')	
    codigo  = models.CharField(u'Código', max_length=1000,blank=True,null=True,help_text=u'Código de incorporação do video')
    
    
    # Audit fields                                                              
    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    class Meta:
        abstract = True
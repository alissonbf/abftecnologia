# -*- coding: utf-8 -*-
"""
Arquivo de classes abstratas de audio

Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
"""

from django.db          import models

class MusicaAbstract(models.Model):
    """
        Modelo de música para ser usada em playlist.
        
        Como usar:
        from multimidia.musica import MusicaAbstract
        
        class Musica(MusicaAbstract):
            historia 	= models.ForeignKey('Historia',related_name='galeria', blank=True, null=True)        
    """
    # Image fields    
    titulo  = models.CharField(verbose_name=u'Titulo', max_length=200,blank=True,null=True,help_text=u'O nome da musica')	
    codigo  = models.CharField(u'Código',max_length=1000,blank=True,null=True,help_text=u'Código de incorporação da playlist')
    
    
    # Audit fields                                                              
    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    class Meta:
        abstract = True
# -*- coding: utf-8 -*-
"""
Arquivo de classes abstratas de apresentações, como prezi ou slideshared

Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
"""

from django.db          import models

class ApresentacaoAbstract(models.Model):
    """
        Modelo de apresentacao para ser usada em galerias de apresentações.
        
        Como usar:
        from multimidia.video import ApresentacaoAbstract
        
        class Apresentacao(ApresentacaoAbstract):
            historia 	= models.ForeignKey('Historia',related_name='galeria', blank=True, null=True)
    """
    # Image fields    
    titulo  = models.CharField(verbose_name=u'Titulo', max_length=200,blank=True,null=True, help_text=u'O nome da apresentação')	
    codigo  = models.CharField(u'Código',max_length=1000,blank=True,null=True,help_text=u'Código de incorporação da apresentação')
    
    
    # Audit fields                                                              
    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    class Meta:
        abstract = True
# -*- coding: utf-8 -*-
#
#  utils/audit.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração com classes de auditoria


from django.db import models

class AuditModel(models.Model):
    """
        Contem campos para auditoria de registro do banco de dados
    """
    # Audit fields                                                              
    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    class Meta:
        abstract = True
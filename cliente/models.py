# -*- coding: utf-8 -*-
#
#  cliente/models.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração dos modelos projeto django, cliente

from django.db                  import models
from django.contrib.auth.models import User


PERFIL_CHOICES  = (
    ('visitante',       'Visitante'),
    ('cliente',         'Cliente'),
    ('funcionario',     'Funcionario'),
    ('administrador',   'Administrador'),
)    

ESTADO_CHOICES  = (
    ('AC',  'Acre'),
    ('AL',  'Alagoas'),
    ('AP',  'Amapá'),
    ('AM',  'Amazonas'),
    ('BA',  'Bahia'),
    ('CE',  'Ceará'),
    ('DF',  'Distrito Federal'),
    ('ES',  'Espirito Santo'),
    ('GO','Goiás'),
    ('MA','Maranhão'),
    ('MT','Mato Grosso'),
    ('MS','Mato Grosso do Sul'),
    ('MG','Minas Gerais'),
    ('PA','Pará'),
    ('PB','Paraiba'),
    ('PR','Paraná'),
    ('PE','Pernambuco'),
    ('PI','Piauí'),
    ('RJ','Rio de Janeiro'),
    ('RN','Rio Grande do Norte'),
    ('RS','Rio Grande do Sul'),
    ('RO','Rondônia'),
    ('RR','Roraima'),
    ('SC','Santa Catarina'),
    ('SP','São Paulo'),
    ('SE','Sergipe'),
    ('TO','Tocantis'),
)


class UserProfile(models.Model):
    """ Atributos adicionais para o usuario """
    user        = models.OneToOneField(User,related_name='user_profile',null=True,blank=True)
    telefone    = models.CharField(u'Telefone', max_length=100,null=True, blank=True)
    cep         = models.CharField(u'CEP', max_length=20,null=True, blank=True)
    estado      = models.CharField(u'Estado', max_length=100,null=True, blank=False,choices=ESTADO_CHOICES)
    cidade      = models.CharField(u'Cidade', max_length=200,null=True, blank=True)
    endereco    = models.CharField(u'Endereço', max_length=300,null=True, blank=True)
    profissao   = models.CharField(u'Área de atuação profissional', max_length=100,null=True, blank=True)
    perfil      = models.CharField(u'Perfil', max_length=100,null=False, blank=False,default=u'visitante',choices=PERFIL_CHOICES)
    
    def __unicode__(self):
        return self.user.username

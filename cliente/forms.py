# -*- coding: utf-8 -*-
#
#  cliente/forms.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem os forms da aplicação django de cliente


from django                     import forms
from django.forms.models        import inlineformset_factory
from django.contrib.auth.models import User

from models             import UserProfile, ESTADO_CHOICES


class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
        
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome:'}),label=u'Nome',max_length=100,required=True,)    
    last_name   = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Sobrenome:'}),label=u'Sobrenome',max_length=100,required=True,)
    email       = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail:'}),label=u'E-mail', max_length=100,required=True)    


class FormCliente(forms.ModelForm):
    class Meta:
        model = UserProfile        
        
    telefone    = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefone:'}),label=u'Telefone',max_length=100,required=True,)
    cep         = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CEP:'}),label=u'CEP',max_length=100,required=True,)
    estado      = forms.CharField(widget=forms.Select(choices=ESTADO_CHOICES,attrs={'class':'form-control'}),label=u'Estado',required=True)
    cidade      = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Cidade:'}),label=u'Cidade',max_length=100,required=True,)
    endereco    = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Endereço:'}),label=u'Endereço',max_length=300,required=True,)
    profissao   = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Profissão:'}),label=u'Profissão',max_length=100,required=True,)


ClienteFormSet = inlineformset_factory(User, UserProfile,FormCliente,exclude=('perfil',), can_delete=False)
    
    
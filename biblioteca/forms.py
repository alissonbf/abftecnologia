# -*- coding: utf-8 -*-
"""
Arquivo dos formularios da aplicação biblioteca

Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
"""


from django import forms

from models import Assinante

class FormAssinante(forms.ModelForm):
    class Meta:
        model   = Assinante
        exclude = ['artigo',]
        
    nome        = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome:'}),max_length=200,required=True,)
    email       = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail:'}), max_length=200,required=True)
    empresa     = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Empresa:'}),max_length=200,required=False,)
    site        = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Website:'}),max_length=200,required=False)
    
    

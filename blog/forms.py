# -*- coding: utf-8 -*-
#
#  blog/forms.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem os forms da aplicação django de blog

from django     import forms
from models     import Comentario

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)
        
    texto    = forms.Field(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Comentário:','rows':'8'}),required=True)    
    

# -*- coding: utf-8 -*-
#
#  forms/views.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem os forms da aplicação django de contato


from django             import forms
from django.core.mail   import send_mail


from django.template        import Context
from django.template.loader import render_to_string, get_template
from django.core.mail       import get_connection, EmailMessage

from abftecnologia.settings import EMAIL_HOST,EMAIL_HOST_USER,EMAIL_HOTS_PASSWORD,EMAIL_PORT,EMAIL_USE_TLS
from models import Mensagem

class FormContato(forms.ModelForm):
    class Meta:
        model = Mensagem
        
    nome        = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nome:'}),max_length=100,required=True,)
    email       = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail:'}), max_length=100,required=True)
    site        = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Website:'}),max_length=100,required=True)
    mensagem    = forms.Field(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Mensagem:','rows':'8'}),required=True)

    def enviar(self):                
        conexao = get_connection(host=EMAIL_HOST,username=EMAIL_HOST_USER,password=EMAIL_HOTS_PASSWORD,port=EMAIL_PORT,user_tls=EMAIL_USE_TLS)
        destino = 'contato@abftecnologia.com.br'
        assunto = '[Contato - ABF Tecnologia]'
        para    = destino
        de      = destino

        texto = {
            'nome':     self.cleaned_data['nome'],
            'email':    self.cleaned_data['email'],
            'site':     self.cleaned_data['site'],
            'mensagem': self.cleaned_data['mensagem'],
        }
        mensagem            = get_template('email/contato.html').render(Context(texto))        
        msg                 = EmailMessage(assunto, mensagem, to=[para,], from_email=de,connection=conexao)
        msg.content_subtype = 'html'
        msg.send()

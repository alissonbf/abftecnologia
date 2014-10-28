# -*- coding: utf-8 -*-
#
#  contato/signals_contato.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração dos sinais projeto django, contato

from django.template        import Context
from django.template.loader import render_to_string, get_template
from django.core.mail       import get_connection, EmailMessage

from abftecnologia.settings import EMAIL_HOST,EMAIL_HOST_USER,EMAIL_HOTS_PASSWORD,EMAIL_PORT,EMAIL_USE_TLS,SITE_URL,EMAIL_REMETENTE

def enviar_newsletter(signal, instance, sender, **kwargs):
    """ Enviar a newsletter para os destinatarios """
    
    newsletter = instance;
    
    texto = {
        'site_url':SITE_URL,
        'email':EMAIL_REMETENTE,
        'assunto': newsletter.assunto,
        'mensagem': newsletter.mensagem,
        'portifolio_item_1': newsletter.portifolio_item_1,
        'portifolio_item_2': newsletter.portifolio_item_2,
        'portifolio_item_3': newsletter.portifolio_item_3,
        'blog_post_all': newsletter.blog_post.all(),
    }
    
    conexao     = get_connection(host=EMAIL_HOST,username=EMAIL_HOST_USER,password=EMAIL_HOTS_PASSWORD,port=EMAIL_PORT,user_tls=EMAIL_USE_TLS)
    FROM_EMAIL  = "%s <%s>"%(newsletter.nome,EMAIL_REMETENTE)
    mensagem    = get_template('email/newsletter.html').render(Context(texto))
            
    for destinatario in newsletter.grupo.destinatario.all():
        msg                 = EmailMessage(newsletter.assunto, mensagem, to=[destinatario.email,], from_email=FROM_EMAIL,connection=conexao)
        msg.content_subtype = 'html'
        msg.send()   
    
# -*- coding: utf-8 -*-
#
#  contato/views.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as views da aplicação django de contato

from django.shortcuts       import render_to_response, get_object_or_404, redirect
from django.template        import RequestContext

from django.core.mail           import BadHeaderError
from django.core.urlresolvers   import reverse

from models     import Contato
from forms      import FormContato

def contato_index(request):
    """ Mostra informações de contato com a empresa """
    
    if request.method=='POST':
        form = FormContato(request.POST)
        if form.is_valid():
            try:
                form.enviar()
                form.save()
            except BadHeaderError:
                mensagem = 'Sua mensagem não pode ser enviada, tente novamente mais tarde.'
                                            
            return redirect(reverse('contato_sucesso'))
    else:
        form = FormContato()
    
    contato     = Contato.objects.all()    
    
    return render_to_response('contato/index.html',locals(),context_instance=RequestContext(request),)

def contato_sucesso(request):
    """ Mostra mensagem enviada com sucesso """
        
    return render_to_response('contato/sucesso.html',locals(),context_instance=RequestContext(request),)

# -*- coding: utf-8 -*-
"""
Arquivo de configuração das views da aplicação biblioteca

Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
"""

from django.shortcuts       import render_to_response, get_object_or_404, redirect
from django.template        import RequestContext

from django.core.urlresolvers   import reverse

from models import Categoria, Artigo, Assinante
from forms  import FormAssinante

def biblioteca_index(request):
    """ Mostra todos os artigos que estão na biblioteca """
    categorias = Categoria.objects.all().order_by('titulo')
    artigos    = Artigo.objects.all().order_by('titulo')
    
    return render_to_response('artigo/index.html',locals(),context_instance=RequestContext(request),)


def biblioteca_artigo(request, slug):
    """
        Mostra informações completas sobre o artigo.
        Salva e redireciona o assinante do artigo para a pagina de download.
    """
    
    artigo    = get_object_or_404(Artigo, slug=slug)
        
    if request.method=='POST':
        form = FormAssinante(request.POST)
        if form.is_valid():
            assinante           = form.save(commit=False)
            assinante.artigo    = artigo
            assinante.save()

            return render_to_response('artigo/download.html',locals(),context_instance=RequestContext(request),)
    else:
        form = FormAssinante()        

    return render_to_response('artigo/detalhe.html',locals(),context_instance=RequestContext(request),)

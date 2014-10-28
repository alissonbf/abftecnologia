# -*- coding: utf-8 -*-
#
#  portifolio/views.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as views da aplicação django de portifolio
#

from django.shortcuts       import render_to_response, get_object_or_404
from django.template        import RequestContext
from django.core.paginator  import Paginator, EmptyPage, PageNotAnInteger

from models             import Item, Categoria

def portifolio_index(request):
    """ Mostra dos os itens do portifolio """
    
    itens_lista = Item.objects.all().order_by('titulo')    
    categorias  = Categoria.objects.all()
    
    paginacao   = Paginator(itens_lista, 8)
    pagina      = request.GET.get('pagina')
    
    try:
        itens = paginacao.page(pagina)
    except PageNotAnInteger:        
        itens = paginacao.page(1) # Se a página não é um inteiro, entregar primeira página.
    except EmptyPage:        
        itens = paginacao.page(paginator.num_pages) # Se a página está fora do intervalo (por exemplo, 9999), entregar última página de resultados.
        
    return render_to_response('item/index.html',locals(),context_instance=RequestContext(request),)


def portifolio_item(request, slug):
    """ Mostra informações completas sobre um item do portifolio """
    item    = get_object_or_404(Item, slug=slug)        
    
    return render_to_response('item/detalhe.html',locals(),context_instance=RequestContext(request),)
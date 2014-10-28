# -*- coding: utf-8 -*-
#
#  home/views.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as views da aplicação django de home
#

from django.shortcuts   import render_to_response
from django.template    import RequestContext

from models    import Slide, Servico, Vantagem, Trabalho
from portifolio.models import Item

def home_index(request):
    slideshow    = Slide.objects.filter(ativo=True).order_by('pk')
    
    servicos     = Servico.objects.all().order_by('pk')
    
    vantagens    = Vantagem.objects.all().order_by('pk')
    
    trabalhos    = Trabalho.objects.all().order_by('ordem')                
    
    return render_to_response('home/index.html',locals(),context_instance=RequestContext(request),)
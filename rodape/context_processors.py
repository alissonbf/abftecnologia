# -*- coding: utf-8 -*-
#
#  rodape/context_processors.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração do context processors da aplicação rodape

from models             import Informacao, RedeSocial
from blog.models        import Post
from biblioteca.models  import Artigo

def conteudo_rodape(request):
    informacao        = Informacao.objects.all().order_by('pk')    
    redes_sociais     = RedeSocial.objects.all().order_by('pk')    
    
    posts             = Post.objects.all().order_by('-created_on')[:2]
    artigos           = Artigo.objects.all().order_by('-created_on')[:8]
    
    
    return {'informacao': informacao, 'redes_sociais':redes_sociais, 'posts': posts,'rodape_artigos':artigos}
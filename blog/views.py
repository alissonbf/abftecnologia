# -*- coding: utf-8 -*-
#
#  blog/views.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as views da aplicação django de blog
#

from django.template            import RequestContext
from django.shortcuts           import render_to_response, get_object_or_404
from django.core.paginator      import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

from models             import Post, Categoria, Comentario

from forms  import FormComentario

NUM_POSTS_PAG = 4 #numero de posts por pagina

def blog_index(request):
    """ Mostra dos os posts do blog"""    
    posts_lista = Post.objects.all().order_by('-created_on')
    categorias  = Categoria.objects.all()

    paginacao   = Paginator(posts_lista, NUM_POSTS_PAG)
    pagina      = request.GET.get('pagina')

    try:
        posts = paginacao.page(pagina)
    except PageNotAnInteger:        
        posts = paginacao.page(1) # Se a página não é um inteiro, entregar primeira página.
    except EmptyPage:        
        posts = paginacao.page(paginator.num_pages) # Se a página está fora do intervalo (por exemplo, 9999), entregar última página de resultados.

    slug = 'home'

    return render_to_response('blog/index.html',locals(),context_instance=RequestContext(request),)
    
def blog_categoria(request, slug):
    """ Mostra dos os posts da categoria """
    categorias  = Categoria.objects.all()
    categoria   = get_object_or_404(Categoria, slug=slug)    
    posts_lista = Post.objects.filter(categoria_id=categoria.pk).order_by('-created_on')

    paginacao   = Paginator(posts_lista, NUM_POSTS_PAG)
    pagina      = request.GET.get('pagina')

    try:
        posts = paginacao.page(pagina)
    except PageNotAnInteger:        
        posts = paginacao.page(1) # Se a página não é um inteiro, entregar primeira página.
    except EmptyPage:        
        posts = paginacao.page(paginator.num_pages) # Se a página está fora do intervalo (por exemplo, 9999), entregar última página de resultados.
    
    return render_to_response('blog/index.html',locals(),context_instance=RequestContext(request),)

def blog_autor(request, slug):
    """ Mostra dos os posts da categoria """    
    categorias  = Categoria.objects.all()
    
    autor       = get_object_or_404(User, username=slug)    
    posts_lista = Post.objects.filter(autor_id=autor.pk).order_by('-created_on')

    paginacao   = Paginator(posts_lista, NUM_POSTS_PAG)
    pagina      = request.GET.get('pagina')

    try:
        posts = paginacao.page(pagina)
    except PageNotAnInteger:        
        posts = paginacao.page(1) # Se a página não é um inteiro, entregar primeira página.
    except EmptyPage:        
        posts = paginacao.page(paginator.num_pages) # Se a página está fora do intervalo (por exemplo, 9999), entregar última página de resultados.
        
    slug = 'home'
    
    return render_to_response('blog/index.html',locals(),context_instance=RequestContext(request),)

def blog_tag(request, slug):
    """ Mostra dos os posts da categoria """    
    categorias  = Categoria.objects.all()
        
    posts_lista = Post.objects.filter(tags__contains=slug).order_by('-created_on')

    paginacao   = Paginator(posts_lista, NUM_POSTS_PAG)
    pagina      = request.GET.get('pagina')

    try:
        posts = paginacao.page(pagina)
    except PageNotAnInteger:        
        posts = paginacao.page(1) # Se a página não é um inteiro, entregar primeira página.
    except EmptyPage:        
        posts = paginacao.page(paginator.num_pages) # Se a página está fora do intervalo (por exemplo, 9999), entregar última página de resultados.
        
    slug = 'home'
    
    return render_to_response('blog/index.html',locals(),context_instance=RequestContext(request),)

def blog_post(request, slug):
    """ Mostra informações completas sobre um post do blog """

    categorias  = Categoria.objects.all()    

    post        = get_object_or_404(Post, slug=slug)    
    comentarios = Comentario.objects.filter(post_id=post.id,status='desbloqueado')    
    
    slug        = post.categoria.slug
    
    
    ## Controla os Comentarios ##    
    if request.method=='POST':
        form = FormComentario(request.POST)
        if form.is_valid():
            comentario          = form.save(commit=False)
            comentario.usuario  = request.user
            comentario.post     = post
            comentario.status   = u'bloqueado'
            comentario.texto    = request.POST['texto']
            comentario.save()
            
            mensagem =  'Seu comentário foi enviado. Aguarde aprovação do moderador.'
    else:
        form = FormComentario()
    
    return render_to_response('blog/post.html',locals(),context_instance=RequestContext(request),)

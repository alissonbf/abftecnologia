# -*- coding: utf-8 -*-
#
#  cliente/views.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Este arquivo contem as views da aplicação django de cliente

from django.shortcuts               import render_to_response, get_object_or_404
from django.template                import RequestContext

from django.http                    import HttpResponseRedirect
from django.core.urlresolvers       import reverse

from django.contrib.auth            import logout
from django.contrib.auth.models     import User
from django.contrib.auth.decorators import login_required

from blog.models            import Comentario

from forms      import FormUser, FormCliente, ClienteFormSet
from models     import UserProfile


@login_required
def cliente_index(request):
    """ Mostra  a home da area do usuario"""
    flag = 'home_usuario'  # Variavel que controla seleção do menu
    
    return render_to_response('cliente/index.html',locals(),context_instance=RequestContext(request),)


@login_required
def cliente_perfil(request):
    """ Mostra  o perfil do usuario para edição"""
    
    flag = 'perfil_usuario' # Variavel que controla seleção do menu
                
    usuario_logado  = get_object_or_404(User,id=request.user.id)
    
    if request.method=='POST':                
        form = FormUser(request.POST,instance=usuario_logado)
        if form.is_valid():
            user_form = form.save()
            cliente_form = ClienteFormSet(request.POST,instance=user_form)
            
            if cliente_form.is_valid():
                usuario = cliente_form.save()
                mensagem = 'Seus perfil foi atualizado com sucesso.'
        else:
            cliente_form    = ClienteFormSet(instance=usuario_logado)
    else:        
        form            = FormUser(instance=usuario_logado)
        cliente_form    = ClienteFormSet(instance=usuario_logado)
        
    return render_to_response('cliente/perfil.html',locals(),context_instance=RequestContext(request),)


@login_required
def cliente_comentarios(request):
    """ Mostra  os comentarios do usuario"""
    flag = 'comentarios_usuario'  # Variavel que controla seleção do menu
    
    comentarios = Comentario.objects.filter(usuario_id=request.user.id).order_by('-created_on','status')
    
    return render_to_response('cliente/comentarios.html',locals(),context_instance=RequestContext(request),)

@login_required
def cliente_sucesso(request):
    """ Mostra  mensagem de cadastra realizado com sucesso """
        
    return render_to_response('cliente/sucesso.html',locals(),context_instance=RequestContext(request),)


def cliente_sair(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_index'))



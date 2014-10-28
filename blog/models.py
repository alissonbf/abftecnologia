# -*- coding: utf-8 -*-
#
#  blog/models.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração dos modelos projeto django, blog

from django.db                  import models
from django.core.urlresolvers   import reverse
from django.contrib.auth.models import User

from image_cropping         import ImageRatioField
from utils.audit            import AuditModel
from utils.singleton        import SingletonModel

from multimidia.video           import VideoAbstract
from multimidia.musica          import MusicaAbstract
from multimidia.apresentacao    import ApresentacaoAbstract

from biblioteca.models  import Artigo
class Categoria(AuditModel):
    """  Categoria dos posts do blog """
    class Meta:
        ordering = ['titulo',]
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    titulo      = models.CharField(u'Titulo', max_length=100)    
    slug        = models.SlugField(u'Link', max_length=100, blank=True, unique=True,help_text=u'Deixe em branco para preenchimento automatico.')

    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('blog_categoria', kwargs={'slug': self.slug})


class Post(AuditModel):
    """  Post do blog """
    class Meta:
        ordering = ['-created_on',]
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'
        
    titulo      = models.CharField(u'Titulo', max_length=70)
    categoria	= models.ForeignKey(Categoria,verbose_name=u'categoria')
    descricao   = models.CharField(u'Descrição',max_length=170)
    texto       = models.TextField(u'Texto')        
    tags        = models.CharField(u'Tags', max_length=100,help_text=u'Não use acentos. Exemplo: internet vendas dinheiro')    
    miniatura   = models.ImageField(null=False, blank=False, upload_to='blog/miniatura',help_text=u'Escolha imagens de 800x500')
    cropping    = ImageRatioField('miniatura', '800x500')    
    autor	= models.ForeignKey(User,verbose_name=u'autor', blank=True, editable=False)
    artigo      = models.ManyToManyField(Artigo, verbose_name=u'artigo', blank=True, null=True,help_text=u'Artigos da biblioteca relacionados ao post.')
    slug        = models.SlugField(u'Link', max_length=100, blank=True, unique=True,help_text=u'Deixe em branco para preenchimento automatico.')
        
    
    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'slug': self.slug})

    # Retorna a nome e sobrenome do autor do post
    def get_user_firstname(self):
        return ("%s %s" % (self.autor.first_name, self.autor.last_name))
    
    get_user_firstname.short_description = 'Autor'

class Video(VideoAbstract):
    """ Video complementar ao post do blog """
    class Meta:
        ordering = ['-created_on',]
        verbose_name = u'Vídeo'
        verbose_name_plural = u'Vídeos'
    
    post 	= models.ForeignKey('Post',related_name='video', blank=True, null=True)

    def __unicode__(self):
        return self.titulo

class Audio(MusicaAbstract):
    """ Playlist complementar ao post do blog """
    class Meta:
        ordering = ['-created_on',]
        verbose_name = u'Audio'
        verbose_name_plural = u'Audios'
    
    post 	= models.ForeignKey('Post',related_name='audio', blank=True, null=True)    

    def __unicode__(self):
        return self.titulo

class Apresentacao(ApresentacaoAbstract):
    """ Apresentação complementar ao post do blog """
    class Meta:
        ordering = ['-created_on',]
        verbose_name = u'Apresentação'
        verbose_name_plural = u'Apresentações'
    
    post 	= models.ForeignKey('Post',related_name='apresentacao', blank=True, null=True)    

    def __unicode__(self):
        return self.titulo


STATUS_CHOICES  = (
    ('bloqueado',       'Bloqueado'),
    ('desbloqueado',    'Desbloqueado'),
) 
    
class Comentario(AuditModel):
    """  Comentario do post """
    class Meta:
        ordering = ['-created_on','status']
        verbose_name = u'Comentario'
        verbose_name_plural = u'Comentarios'

    usuario = models.ForeignKey(User,verbose_name=u'usuario', null=True, blank=True, editable=False)
    post    = models.ForeignKey(Post,verbose_name=u'post', null=True, blank=True, editable=False)
    texto   = models.TextField(u'Texto', blank=True, editable=False)
    status  = models.CharField(u'Status', max_length=100,null=False, default=u'bloqueado', blank=False,choices=STATUS_CHOICES)
    
    def __unicode__(self):
        return self.texto
    
    # Retorna a nome e sobrenome do autor do comentario
    def get_user_firstname(self):
        return ("%s %s" % (self.usuario.first_name, self.usuario.last_name))
    
    get_user_firstname.short_description = 'Usuario'
    
#SIGNAL
from django.db.models       import signals
from utils.signals_comuns   import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Categoria)
signals.pre_save.connect(slug_pre_save, sender=Post)
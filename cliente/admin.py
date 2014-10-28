# -*- coding: utf-8 -*-
#
#  cliente/admin.py
#  
#  Copyright 2014 Alisson Barbosa Ferreira <alissonbf@hotmail.com>
#
#  Arquivo de configuração do admin do projeto django, cliente

from django.contrib             import admin
from django.contrib.auth.admin  import UserAdmin as OriginalUserAdmin
from django.contrib.auth.models import User

from cliente.models             import UserProfile

class UserProfileInline(admin.StackedInline):
    """ O seu perfil será editado como forma in-line """
    model = UserProfile
    can_delete = False
    
class UserAdmin(OriginalUserAdmin):
    """ Basta adicionar inlines à classe UserAdmin originais """
    inlines = [UserProfileInline, ]
 
try:
    admin.site.unregister(User)
finally:
    admin.site.register(User, UserAdmin)
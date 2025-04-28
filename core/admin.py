from django.contrib import admin
from .models import Usuario, Postagem, Like, Seguidor

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):

    list_display =      ('id', 'username', 'email', 'is_staff', 'is_active')
    search_fields =     ('username', 'email')
    list_filter =       ('is_staff', 'is_active')

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):

    list_display =      ('id', 'autor_postagem', 'texto_postagem', 'data_criacao_postagem')
    search_fields =     ('autor_postagem__username', 'texto_postagem')
    list_filter =       ('data_criacao_postagem',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display =      ('id', 'usuario_like', 'postagem_like', 'data_like')
    search_fields =     ('usuario_like__username', 'postagem_like__texto_postagem')

@admin.register(Seguidor)
class SeguidorAdmin(admin.ModelAdmin):

    list_display =      ('id', 'seguidor', 'seguindo', 'seguidor_data')
    search_fields =     ('seguidor__username', 'seguindo__username')

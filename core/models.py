from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Postagem(models.Model):

    autor_postagem = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='posts'
    )

    texto_postagem = models.TextField()

    imagem_postagem = models.ImageField(
        upload_to='posts/', 
        blank=True, 
        null=True
    )

    data_criacao_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Postado por {self.autor_postagem.username} em {self.data_criacao_postagem}"

class Like(models.Model):

    usuario_like = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE
    )

    postagem_like = models.ForeignKey(
        Postagem, 
        on_delete=models.CASCADE
    )

    data_like = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario_like', 'postagem_like')

    def __str__(self):
        return f"{self.usuario_like.username} curtiu a postagem {self.postagem_like.id}"


class Seguidor(models.Model):

    seguidor = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='following'
    )

    seguindo = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='followers'
    )
    
    seguidor_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('seguidor', 'seguindo')

    def __str__(self):
        return f"{self.seguidor.username} seguiu {self.seguindo.username}"

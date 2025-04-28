from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only = True
    )

    class Meta:

        model = Usuario

        fields = [
            'id', 'username', 'email', 'password'
        ]

    def create(self, dados):

        user = Usuario(
            username =  dados['username'],
            email =     dados['email'],
        )
        user.set_password(
            dados['password']
        )
        user.save()

        return user

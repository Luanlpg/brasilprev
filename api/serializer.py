from rest_framework import serializers

from .models import UserModel

from .models import AccountModel

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador de clientes.
    """
    class Meta:
        model = UserModel
        depth = 1
        fields = [
            'username',
            'nome',
            'sobrenome',
            'email',
            'cpf',
            'cidade',
            'bairro',
            'complemento',
            'dataNascimento',
            'estado',
            'numero',
            'pais',
            'password',
            'rua'
            ]

class AccountSerializer(serializers.ModelSerializer):
    """
    Serializador de conta.
    """
    class Meta:
        model = UserModel
        depth = 1
        fields = [
            'cpf',
            'id',
            'saldo'
            ]
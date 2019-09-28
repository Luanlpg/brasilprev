from rest_framework import serializers

from .models import UserModel
from .models import AccountModel
from .models import ExtractModel

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador de usuarios.
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
        model = AccountModel
        depth = 1
        fields = [
            'cpf',
            'id',
            'saldo'
            ]


class ExtractSerializer(serializers.ModelSerializer):
    """
    Serializador de extrato.
    """
    class Meta:
        model = ExtractModel
        depth = 1
        fields = [
            'conta',
            'data',
            'descricao',
            'valor'
            ]

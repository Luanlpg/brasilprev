from rest_framework import serializers

from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador de clientes.
    """
    class Meta:
        model = UserModel
        depth = 1
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'date_joined',
            'token',
            'cpf',
            'city',
            'district',
            'complement',
            'date_of_birth',
            'state',
            'number',
            'country',
            'password',
            'street'
            ]

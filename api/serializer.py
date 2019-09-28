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
            'email'
            ]

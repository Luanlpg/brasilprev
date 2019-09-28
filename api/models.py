from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import uuid


class UserModel(models.Model):
    """=========================================================================
    Model de Usuário.
    ========================================================================="""
    cpf = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=60, unique=True, null=True)
    nome = models.CharField(max_length=40, null=False)
    sobrenome = models.CharField(max_length=40, null=False)
    email = models.EmailField(max_length=300, unique=True, null=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    cidade = models.CharField(max_length=120, null=True)
    bairro = models.CharField(max_length=150, null=True)
    complemento = models.CharField(max_length=150, null=True)
    dataNascimento = models.CharField(max_length=150, null=False)
    estado = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)
    pais = models.CharField(max_length=100, null=True)
    numero = models.IntegerField(null=True)
    password = models.CharField(max_length=150, null=False)
    rua = models.CharField(max_length=150, null=True)

    def save(self, *args, **kwargs):
        """
        Cria username
        """
        self.username = str(self.cpf)
        User.objects.create(
            username = self.username,
            email = self.email,
            first_name = self.nome,
            last_name = self.sobrenome
        )
        super(UserModel, self).save(*args, **kwargs)


class AccountModel(models.Model):
    cpf = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    saldo = models.FloatField(null=True)



class ExtractModel(models.Model):
    conta = models.ForeignKey(AccountModel, on_delete=models.PROTECT)
    data = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255, null=True)
    valor = models.FloatField()


class TransactionModel(models.Model):
    contaDestino = models.ForeignKey(AccountModel, on_delete=models.PROTECT, related_name='origin')
    contaOrigin = models.ForeignKey(AccountModel, on_delete=models.PROTECT, related_name='destiny', null=True)
    type_transactions = models.CharField(max_length=30)
    valor = models.FloatField()

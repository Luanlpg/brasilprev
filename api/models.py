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
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    email = models.EmailField(max_length=300, unique=True, null=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=120, null=True)
    district = models.CharField(max_length=150, null=True)
    complement = models.CharField(max_length=150, null=True)
    date_of_birth = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=100, null=True)
    number = models.IntegerField(null=True)
    country = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=150, null=False)
    street = models.CharField(max_length=150, null=True)

    def save(self, *args, **kwargs):
        """
        Cria username
        """
        self.username = str(self.cpf)
        super(UserModel, self).save(*args, **kwargs)


class AccountModel(models.Model):
    cpf = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    conta = models.IntegerField()
    saldo = models.FloatField()


class TransactionModel(models.Model):
    account_origin = models.ForeignKey(AccountModel, on_delete=models.PROTECT, related_name='origin')
    account_destiny = models.ForeignKey(AccountModel, on_delete=models.PROTECT, related_name='destiny')
    type_transactions = models.CharField(max_length=30)
    value = models.FloatField()

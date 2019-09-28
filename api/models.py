from django.db import models
from django.utils import timezone

import uuid


class UserModel(models.Model):
    """=========================================================================
    Model de Usuário.
    ========================================================================="""
    username = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    email = models.EmailField(max_length=300, unique=True, null=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    token = models.CharField(default='-- -- --', max_length=300)
    cpf = models.IntergerField(max_length=11)
    city = models.CharField(max_length=120, null=True)
    district = models.CharField(max_length=150, null=True)
    complement = models.CharField(max_length=150, null=True)
    date_of_birth = models.CharField(max_lenth=150, null=False)
    state = models.CharField(max_length=100, null=True)
    number = models.IntergerField(null=True)
    country = models.CharField(max_length=100, null=True)  
    password = models.CharField(max_length=150, null=False)
    street = models.CharField(max_length=150, null=True)

    def save(self, *args, **kwargs):    
        """
        Cria uuid e token
        """
        self.username = str(self.cpf)   
        self.token = uuid.uuid4().hex
        super(UserModel, self).save(*args, **kwargs)

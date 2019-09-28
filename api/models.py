from django.db import models
from django.utils import timezone

import uuid


class UserModel(models.Model):
    """=========================================================================
    Model de Usuário.
    ========================================================================="""
    username = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=300, unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    token = models.CharField(default='-- -- --', max_length=300)

    def save(self, *args, **kwargs):
        """
        Cria uuid e token
        """
        self.token = uuid.uuid4().hex
        super(UserModel, self).save(*args, **kwargs)

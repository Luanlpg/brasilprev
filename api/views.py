from django.shortcuts import render

from .serializer import UserSerializer
from .serializer import AccountSerializer
from .serializer import ExtractSerializer

from .models import UserModel
from .models import AccountModel

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.permissions import IsAuthenticated

import time
import requests
import json

class UserListView(APIView):
    """=========================================================================\n
    View que lista e cadastra users.\n
    ========================================================================="""
    serializer_class = UserSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(UserModel.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    """=========================================================================\n
    View que mostra, altera e apaga user.\n
    ========================================================================="""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_user(self, cpf):
        try:
            return UserModel.objects.get(cpf=cpf)
        except UserModel.DoesNotExist:
            raise Http404

    def get(self, request, cpf, format=None):
        user = self.get_user(cpf)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, cpf, format=None):
        user = self.get_user(cpf)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExtractDetailView(APIView):
    """
    View que mostra e apaga extrato.
    """
    serializer_class = ExtractSerializer

    def get_account(self, account):
        try:
            return AccountModel.objects.get(account=account)
        except AccountModel.DoesNotExist:
            raise Http404

    def get(self, request, account, format=None):
        serializer = self.serializer_class(ExtractModel.objects.filter(conta=account), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, account, format=None):
        extract = self.get_account(account)
        extract.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExtractView(APIView):
    """=========================================================================\n
    View que lista e cadastra extrato.\n
    ========================================================================="""
    serializer_class = ExtractSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountView(APIView):
    """=========================================================================\n
    View que mostra, altera e apaga conta.\n
    ========================================================================="""

    serializer_class = AccountSerializer
    # permission_classes = [IsAuthenticated]

<<<<<<< HEAD
    def post(self, requests, format=None):
=======
    def post(self, requests,format=None):
>>>>>>> 6eb3ac129bd6282a6a454e8ae75e0cc7b4122cf8
        serializer = self.serializer_class(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response('{ message: "success" }', status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_account(self, id):
        try:
            return UserModel.objects.get(cpf=cpf)
        except UserModel.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        account = self.get_account(id)
        serializer = self.serializer_class(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

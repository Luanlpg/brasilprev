from django.shortcuts import render

from .serializer import UserSerializer

from .serializer import AccountSerializer

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


class AccountView(APIView):
    """=========================================================================\n
    View que mostra, altera e apaga conta.\n
    ========================================================================="""

    serializer_class = AccountSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, requests, format=None):
        serializer = self.serializer_class(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response('{ message: "success" }', status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_account(self, id):
        try:
            return UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        account = self.get_account(id)
        serializer = self.serializer_class(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddSaldoView(APIView):
    
    """=========================================================================\n
    View que adiociona saldo na conta.\n
    ========================================================================="""

    serializer_class = AccountSerializer
    # permission_classes = [IsAuthenticated]

    def get_account(id):
        try:
            return UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            raise Http404
    
    def post(self, requests, format=None):
        account_view = AccountView()
        account = account_view.get_account(requests.data['conta'])
        requests.data['saldo'] += account.valor
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailView(APIView):
    """=========================================================================\n
    View que deleta e retorna a conta.\n
    ========================================================================="""
    serializer_class = AccountSerializer
    # permission_classes = [IsAuthenticated]

    def get_account(id):
        try:
            return UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        account = this.get_account(id)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, requests, id, format=None):
        account = self.get_account(id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransferView(APIView):
    """=========================================================================\n
    View que deleta e retorna a conta.\n
    ========================================================================="""
    # permission_classes = [IsAuthenticated]

    def post(self, requests, format=None):
        accountView = AccountView()
        account_des = accountView.get_account(requests.data['contaDestino'])
        account_ori = accountView.get_account(requests.data['contaOrigem'])
        if account_ori.saldo >= requests.data['valor']:
            account_des.saldo += requests.data['valor']
            account_ori.saldo -= requests.data['valor']
            account_des.save()
            account_ori.save()

            return Response('{ message: "success" }', status=status.HTTP_201_CREATED)
        
        return Response('{ message: "account without balance" }', status=status.HTTP_400_BAD_REQUEST)


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


<<<<<<< HEAD
class ExtractDetailView(APIView):
    """
    View que mostra e apaga extrato.
    """
    serializer_class = ExtractSerializer

    def get_transitions(self, account):
        try:
            return AccountModel.objects.get(account=account)
        except AccountModel.DoesNotExist:
            raise Http404

    def get(self, request, account, format=None):
        extract = self.get_transitions(account)
        serializer = self.serializer_class(extract)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, account, format=None):
        # não vejo de delete
        return Response('{"message": "success"}', status=status.HTTP_204_NO_CONTENT)
=======
class AccountView(APIView):
    """=========================================================================\n
    View que mostra, altera e apaga conta.\n
    ========================================================================="""

    serializer_class = AccountSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, format=None, requests):
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
>>>>>>> d65cf05c24d0c83c6ef1e9566737198d3ef78967

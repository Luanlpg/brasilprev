from django.urls import path
from django.urls import include

from rest_framework import routers

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('auth', obtain_jwt_token),
    path('refresh-token', refresh_jwt_token),
    path('login', views.LoginView.as_view()),
    path('user', views.UserListView.as_view()),
    path('account', views.AccountView.as_view()),
    path('account/adicionarSaldo', views.AddSaldoView.as_view()),
    path('account/<int:id>', views.AccountDetailView.as_view()),
    path('transferir', views.TransferView.as_view()),
    path('user/<str:cpf>', views.UserDetailView.as_view())
]

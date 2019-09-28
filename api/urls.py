from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from django.urls import include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_jwt_token(),

]

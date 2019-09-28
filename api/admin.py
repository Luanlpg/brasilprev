from django.contrib import admin

from .models import UserModel
from .models import AccountModel
from .models import ExtractModel
from .models import TransactionModel


admin.site.register(UserModel)
admin.site.register(AccountModel)
admin.site.register(ExtractModel)
admin.site.register(TransactionModel)

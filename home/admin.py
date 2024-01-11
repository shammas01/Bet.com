from django.contrib import admin
from . models import BetModel,WalletModel,Slot
# Register your models here.

admin.site.register(BetModel)
admin.site.register(Slot)
admin.site.register(WalletModel)
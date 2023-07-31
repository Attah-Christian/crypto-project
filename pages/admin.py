from django.contrib import admin
from .models import Enquirie, Number
# Register your models here.

class EnquirieAdmin(admin.ModelAdmin):
    list_display = ("btc_wallet", "eth_wallet", "usdterc20_wallet", "usdttrc20_wallet")
    list_display_links = ("btc_wallet", "eth_wallet", "usdterc20_wallet", "usdttrc20_wallet")


class NumberAdmin(admin.ModelAdmin):
    list_display = ("balance", "profit1", "profit2", "profit3", "profit4", "profit5")
    list_display_links = ("balance", "profit1", "profit2", "profit3", "profit4", "profit5")


admin.site.register(Enquirie, EnquirieAdmin)
admin.site.register(Number, NumberAdmin)

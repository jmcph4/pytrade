from django.contrib import admin

from .models import Trader, Market, Order

admin.site.register(Trader)
admin.site.register(Market)
admin.site.register(Order)


from django.contrib import admin

from .models import Trader, Market, Order, Participant

admin.site.register(Trader)
admin.site.register(Market)
admin.site.register(Order)
admin.site.register(Participant)


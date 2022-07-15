from django.contrib import admin
from .models import StocksItem, PurchaseOrder

# Register your models here.
admin.site.register(StocksItem)
admin.site.register(PurchaseOrder)
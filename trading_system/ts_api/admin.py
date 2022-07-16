from django.contrib import admin
from .models import StocksItem, PurchaseOrder, UserPortfolio

# Register your models here.
admin.site.register(StocksItem)
admin.site.register(PurchaseOrder)
admin.site.register(UserPortfolio)
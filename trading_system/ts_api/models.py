from django.db import models

# Create your models here.

class StocksItem(models.Model):
    stock_id = models.BigAutoField(primary_key=True)
    stock_name = models.CharField(max_length=50)
    stock_price = models.FloatField()

class PurchaseOrder(models.Model):
    cart_id = models.BigAutoField(primary_key=True)
    stock_name = models.CharField(max_length=50)
    stock_price = models.FloatField()
    stock_quantity = models.IntegerField()
    total_price = models.FloatField()
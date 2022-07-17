from rest_framework import serializers
from .models import StocksItem, PurchaseOrder, UserPortfolio

class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StocksItem
        fields = ["stock_name", "stock_price"]

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        # fields = ["stock_name", "stock_price", "stock_quantity", "total_price", "user_name"]
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPortfolio
        fields = ["purchase_id", "user_name"]
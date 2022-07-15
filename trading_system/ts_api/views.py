#from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import PurchaseOrder, StocksItem
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StockItem(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        stock_name = data.get('stock_name')
        stock_price = data.get('stock_price')

        stock_data = {
            'stock_name': stock_name,
            'stock_price': stock_price,
        }

        stock_item = StocksItem.objects.create(**stock_data)

        data = {
            'message': f'New stocks added to DB with stock id: {stock_item.stock_id}'
        }

        return JsonResponse(data, status=201)

    def get(self, request, stock_name):
        # data = json.loads(request.body.decode('utf-8'))
        # print(data)
        # s_name = data.get('stock_name')

        stock_data = StocksItem.objects.get(stock_name=stock_name)

        data = {
            'stock_name': stock_data.stock_name,
            'stock_price': stock_data.stock_price,
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class OrderCart(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        stock_name = data.get('stock_name')
        stock_quantity = data.get('quantity')
        try:
            stock_data = StocksItem.objects.get(stock_name=stock_name)
            
            data = {
                'stock_name': stock_data.stock_name,
                'stock_price': stock_data.stock_price,
                'stock_quantity': stock_quantity,
                'total_price': float(stock_quantity) * stock_data.stock_price,
            }

            purchase_order = PurchaseOrder.objects.create(**data)

            data = {
                'message': f'New purchase order added to DB with cart id: {purchase_order.cart_id}'
            }
            return JsonResponse(data, status=201)
        except StocksItem.DoesNotExist: 
            data = {
                'message': f'Stock name: {stock_name} does not exist.'
            }

            return JsonResponse(data, status=202)

    def get(self, request, cart_id):
        
        stock_data = PurchaseOrder.objects.get(cart_id=cart_id)

        data = {
            'stock_name': stock_data.stock_name,
            'stock_price': stock_data.stock_price,
            'quantity': stock_data.stock_quantity,
            'total': stock_data.total_price,
        }

        return JsonResponse(data)
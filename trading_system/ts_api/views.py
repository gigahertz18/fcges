#from django.shortcuts import render
from django import views
from django.views import View
from django.http import JsonResponse
import json
from .models import PurchaseOrder, StocksItem, UserPortfolio
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from .serializers import StocksSerializer, PurchaseSerializer, UserSerializer

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
        user_name = data.get('username')
        try:
            stock_data = StocksItem.objects.get(stock_name=stock_name)
            
            purchase_data = {
                'stock_name': stock_data.stock_name,
                'stock_price': stock_data.stock_price,
                'stock_quantity': stock_quantity,
                'total_price': float(stock_quantity) * stock_data.stock_price,
                'user_name': user_name,
            }

            purchase_order = PurchaseOrder.objects.create(**purchase_data)

            user_data = {
                'purchase_id': purchase_order.cart_id,
                'user_name': user_name,
            }

            portfolio_data = UserPortfolio.objects.create(**user_data)
            response_data = {
                'message': f'New purchase order added to DB with cart id: {purchase_order.cart_id} under user id: {portfolio_data.user_name}'
            }
            return JsonResponse(response_data, status=201)
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


@method_decorator(csrf_exempt, name='dispatch')
class ShowPortfolio(View):
    def get(self, request, username):
        portfolio_data = UserPortfolio.objects.filter(user_name=username)
        total_investment = 0
        for user_data in portfolio_data:
            purchase_data = PurchaseOrder.objects.get(cart_id=user_data.purchase_id)
            total_investment += purchase_data.total_price

        response_data = {
            'username': username,
            'total_investment': total_investment
        }

        return JsonResponse(response_data)

    def get(self, request, username, stockname):
        portfolio_data = UserPortfolio.objects.filter(user_name=username)
        total_investment = 0

        for user_data in portfolio_data:
            purchase_data = PurchaseOrder.objects.get(cart_id=user_data.purchase_id)

            if purchase_data.stock_name == stockname:
                total_investment += purchase_data.total_price
            else:
                pass

        response_data = {
            'username': username,
            'stockname': stockname,
            'total_investment': total_investment
        }

        return JsonResponse(response_data)

class StockItemView(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def post(self, request):

        stock_name = request.data.get('stock_name')
        stock_price = request.data.get('stock_price')

        stock_data = {
            'stock_name': stock_name,
            'stock_price': stock_price,
        }

        serialized_data = StocksSerializer(data=stock_data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        stock_data = StocksItem.objects.get(stock_name=request.query_params.get('stock_name'))

        serialized_data = StocksSerializer(stock_data)

        return Response(serialized_data.data, status=status.HTTP_200_OK)

class OrderCartView(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def post(self, request):

        stock_name = request.data.get('stock_name')
        stock_quantity = request.data.get('quantity')
        user_name = request.data.get('username')
        try:
            stock_data = StocksItem.objects.get(stock_name=stock_name)
            
            purchase_data = {
                'stock_name': stock_data.stock_name,
                'stock_price': stock_data.stock_price,
                'stock_quantity': stock_quantity,
                'total_price': float(stock_quantity) * stock_data.stock_price,
                'user_name': user_name,
            }

            purchase_data = PurchaseSerializer(data=purchase_data)

            if purchase_data.is_valid():
                purchase_data.save()
                user_data = {
                    'purchase_id': purchase_data.data['cart_id'],
                    'user_name': user_name,
                }
                portfolio_data = UserSerializer(data=user_data)

                if portfolio_data.is_valid():
                    portfolio_data.save()
                return Response(purchase_data.data, status=status.HTTP_201_CREATED)

            return Response(purchase_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except StocksItem.DoesNotExist: 
            data = {
                'message': f'Stock name: {stock_name} does not exist.'
            }

            return Response(data, status=status.HTTP_404_NOT_FOUND)

        
    def get(self, request):
        purchase_data = PurchaseOrder.objects.get(cart_id=request.query_params.get('cart_id'))

        data = PurchaseSerializer(purchase_data)

        return Response(data.data, status=status.HTTP_200_OK)

class ShowPortfolioView(View):
    authentication_classes = []
    permission_classes = []
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    def get(self, request, username):
        portfolio_data = UserPortfolio.objects.filter(user_name=username)
        total_investment = 0
        for user_data in portfolio_data:
            purchase_data = PurchaseOrder.objects.get(cart_id=user_data.purchase_id)
            total_investment += purchase_data.total_price

        response_data = {
            'username': username,
            'total_investment': total_investment
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def get(self, request, username, stockname):
        portfolio_data = UserPortfolio.objects.filter(user_name=username)
        total_investment = 0

        for user_data in portfolio_data:
            purchase_data = PurchaseOrder.objects.get(cart_id=user_data.purchase_id)

            if purchase_data.stock_name == stockname:
                total_investment += purchase_data.total_price
            else:
                pass

        response_data = {
            'username': username,
            'stockname': stockname,
            'total_investment': total_investment
        }

        return Response(response_data, status=status.HTTP_200_OK)
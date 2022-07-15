from django.urls import path
from .views import StockItem, OrderCart

urlpatterns = [
    path('add-stocks/', StockItem.as_view()),
    path('stocks/<str:stock_name>', StockItem.as_view()),
    path('add-to-cart/', OrderCart.as_view()),
    path('cart/<int:cart_id>', OrderCart.as_view()),
]
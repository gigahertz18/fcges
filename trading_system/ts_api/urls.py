from django.urls import path
from .views import StockItem, OrderCart, ShowPortfolio, StockItemView, OrderCartView, ShowPortfolioView

urlpatterns = [
    path('add-stocks/', StockItem.as_view()),
    path('stocks/<str:stock_name>', StockItem.as_view()),
    path('add-to-cart/', OrderCart.as_view()),
    path('cart/<int:cart_id>', OrderCart.as_view()),
    path('portfolio/<str:username>', ShowPortfolio.as_view()),
    path('portfolio/<str:username>/<str:stockname>', ShowPortfolio.as_view()),
    path('stocksview/', StockItemView.as_view()),
    path('stocksview/', StockItemView.as_view()),
    path('cart/', OrderCartView.as_view()),

]
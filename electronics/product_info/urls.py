from django.urls import path, include
from rest_framework.routers import SimpleRouter
from product_info.views import SalesView

sales_router = SimpleRouter()
sales_router.register('sales', SalesView, basename='sales')

urlpatterns = [
    path('', include(sales_router.urls)),
]

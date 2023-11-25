from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')
router.register(r'purchase_orders', PurchaseOrderViewSet, basename='purchase_order')

urlpatterns = [
    path('', include(router.urls)),
]


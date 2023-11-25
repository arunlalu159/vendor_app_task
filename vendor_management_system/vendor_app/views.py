from datetime import timezone
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from .utils import update_vendor_performance

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        update_vendor_performance(vendor)
        serializer = self.get_serializer(vendor)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def historical_performance(self, request, pk=None):
        vendor = self.get_object()
        historical_performance = HistoricalPerformance.objects.filter(vendor=vendor)
        serializer = HistoricalPerformanceSerializer(historical_performance, many=True)
        return Response(serializer.data)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        purchase_order = self.get_object()
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        update_vendor_performance(purchase_order.vendor)
        return Response({'message': 'Purchase order acknowledged successfully.'})

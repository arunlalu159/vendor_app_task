from django.db.models import Count, Avg
from django.utils import timezone
from .models import HistoricalPerformance

def update_vendor_performance(vendor):
    completed_orders = vendor.purchaseorder_set.filter(status='completed')
    total_completed_orders = completed_orders.count()

    # On-Time Delivery Rate
    on_time_delivery_count = completed_orders.filter(delivery_date__lte=timezone.now()).count()
    on_time_delivery_rate = (on_time_delivery_count / total_completed_orders) * 100 if total_completed_orders > 0 else 0

    # Quality Rating Average
    quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg']

    # Average Response Time
    response_times = completed_orders.exclude(acknowledgment_date=None).annotate(
        response_time=Count('acknowledgment_date') - Count('issue_date')
    ).aggregate(Avg('response_time'))['response_time__avg']
    average_response_time = response_times if response_times else 0

    # Fulfilment Rate
    successful_fulfillment_count = completed_orders.filter(issue_date__lte=timezone.now()).count()
    fulfillment_rate = (successful_fulfillment_count / total_completed_orders) * 100 if total_completed_orders > 0 else 0
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_avg
    vendor.average_response_time = average_response_time
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()

    HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=average_response_time,
        fulfillment_rate=fulfillment_rate
    )

from django.contrib import admin
from vendor_app.models import Vendor,PurchaseOrder,HistoricalPerformance
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display=['name','contact_details','vendor_code']



class PurchaseAdmin(admin.ModelAdmin):
    list_display=['vendor','po_number','order_date','delivery_date']

class HPAdmin(admin.ModelAdmin):
    list_display=['vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']




admin.site.register(Vendor,VendorAdmin),
admin.site.register(PurchaseOrder,PurchaseAdmin)
admin.site.register(HistoricalPerformance,HPAdmin),



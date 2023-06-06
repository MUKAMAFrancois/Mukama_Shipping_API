from django.contrib import admin
from orders.models import Electronic_Item



# Register your models here.

@admin.register(Electronic_Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['customer','description','id','weight','electronic','district_name']
    list_filter=['electronic','price','district_name','be_shipped']
    search_fields=('customer',)


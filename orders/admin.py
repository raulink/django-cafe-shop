from django.contrib import admin

# Register your models here.
from .models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0  #No crear extra campos


class OrderAmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInline]
    """ list_display = ['id', 'user', 'is_active', 'order_date', 'created_at']
    list_filter = ['is_active', 'order_date']
    search_fields = ['id', 'user__username', 'user__email', 'order_date']
    date_hierarchy = 'order_date'
    readonly_fields = ['created_at'] """
    

admin.site.register(Order,OrderAmin)

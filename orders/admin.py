from django.contrib import admin
from .models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'address', 'postal_code',
                    'city', 'created',  'updated', 'paid', 'id']

    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

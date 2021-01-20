from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total', 'select_date',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'original_bag',
                       'stripe_pid',)
    # fields allows to specify the order of the fields in the admin interface
    fields = ('order_number', 'date',
              'user_profile', 'full_name',
              'email', 'phone_number', 'town_or_city',
              'street_address1', 'street_address2',
              'postcode', 'county', 'country',
              'order_total', 'original_bag',
              'stripe_pid',)
    # restrict the columns that show up in the order list to only few key items
    list_display = ('order_number', 'date',
                    'full_name', 'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)


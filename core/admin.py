from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'state']

admin.site.register(Category, CategoryAdmin)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'calories', 'photo', 'state']
    list_filter = ['category', 'state', 'price', 'calories']
    list_editable = ['category', 'price', 'calories', 'state']

admin.site.register(Item, ItemAdmin)
class TableAdmin(admin.ModelAdmin):
    list_display = ['number', 'description', 'capacity']
    list_filter = ['number']
    list_editable = ['description', 'capacity']

admin.site.register(Table, TableAdmin)
# class OrderAdmin(admin.ModelAdmin):
#    list_display = ['number_order', 'date_order', 'state', 'table']
#    list_filter = ['date_order', 'state', 'table']
#    list_editable = ['state', 'table']
# admin.site.register(OrderAdmin)
# class OrderDetailAdmin(admin.ModelAdmin):
#    list_display = ['order', 'item', 'quantity']
#    list_filter = ['order']
#    list_editable = ['quantity']
# admin.site.register(OrderDetail, OrderDetailAdmin)

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
class OrderDetailAdmin(admin.ModelAdmin):
    inlines = (OrderDetailInline,)
admin.site.register(Order, OrderDetailAdmin)
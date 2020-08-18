from rest_framework import serializers
from .models import Table, Category, Item, Order, OrderDetail


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['number', 'capacity', 'description']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'photo', 'state']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'category', 'description', 'ingredients', 'price', 'calories', 'photo', 'state']


class CategoryItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'item']


class OrderDetailSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name')
    item_price = serializers.CharField(source='item.price')

    class Meta:
        model = OrderDetail
        fields = ['item', 'item_name', 'item_price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    orderdetail_order = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['number_order', 'date_order', 'orderdetail_order']


class TableOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Table
        fields = ['number', 'capacity', 'description', 'order']

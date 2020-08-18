from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .models import Table, Category, Item, Order
from .serializers import TableSerializer, CategorySerializer, ItemSerializer, CategoryItemSerializer, \
    TableOrderSerializer


class TableAllViewset(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = (AllowAny,)


class CategoryAllViewset(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class ItemAllViewset(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (AllowAny,)


class CategoryItemAllViewset(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryItemSerializer
    permission_classes = (AllowAny,)


class CategoryItemIdViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryItemSerializer
    permission_classes = (AllowAny,)


class TableOrderAllViewset(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableOrderSerializer
    permission_classes = (AllowAny,)


class TableOrderIdViewset(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableOrderSerializer
    permission_classes = (AllowAny,)

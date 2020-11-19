from rest_framework import serializers
from .models import Products, Categories, Customers, Orders, OrdersDetails

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'nameProduct', 'price', 'stock', 'discontinued', 'category')

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('__all__')

class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ('__all__')

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')

class OrdersDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrdersDetails
        fields = ('__all__')
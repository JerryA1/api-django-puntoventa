from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductsSerializer, CategoriesSerializer, CustomersSerializer, OrdersSerializer, OrdersDetailsSerializer
from .models import Products, Categories, Customers, Orders, OrdersDetails

# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductsSerializer
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('id')
    serializer_class = CategoriesSerializer

class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all().order_by('id')
    serializer_class = CustomersSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('id')
    serializer_class = OrdersSerializer

class OrdersDetailsViewSet(viewsets.ModelViewSet):
    queryset = OrdersDetails.objects.all().order_by('id')
    serializer_class = OrdersDetailsSerializer
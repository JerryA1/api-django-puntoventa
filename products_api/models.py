from django.db import models

class Categories(models.Model):
    """ Modelo base de datos para categories en el sistema """
    nameCategory = models.CharField(max_length=255)

    def __str__(self):
        return self.nameCategory

class Products(models.Model):
    """ Modelo base de datos para productos en el sistema """
    nameProduct = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    discontinued = models.BooleanField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameProduct

class Customers(models.Model):
    nameCustomer = models.CharField(max_length=255)
    addCustomer = models.CharField(max_length=255)
    emailCustomer = models.CharField(max_length=255)
    phoneCustomer = models.CharField(max_length=255)

    def __str__(self):
        return self.nameCustomer

class Orders(models.Model):
    dateOrder = models.DateTimeField()
    shippedDate = models.DateTimeField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def __str__(self):
        return self.dateOrder

class OrdersDetails(models.Model):
    price = models.FloatField()
    discount = models.FloatField()
    quantity = models.FloatField()
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.order
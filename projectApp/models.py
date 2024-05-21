from django.db import models

# Create your models here.

class Products(models.Model):
    product_id = models.CharField(max_length=4, unique=True, primary_key=True)
    product_name = models.CharField(max_length=100)
    unit_price = models.FloatField()
    region = models.CharField(max_length=100)

class Customers(models.Model):
    customer_id = models.CharField(max_length=4, unique=True, primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)


class Orders(models.Model):
    order_id = models.IntegerField()
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, to_field='product_id')
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, to_field='customer_id')
    date_of_sale = models.DateTimeField()
    quantity = models.FloatField()
    discount = models.FloatField()
    shipping_cost = models.FloatField()
    payment_method = models.CharField(max_length=100)
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customers, Orders, Products
# from django.core import serializers

class DataSerializer(serializers.Serializer):
    total_customers = serializers.DecimalField(max_digits=5, decimal_places=2)
    total_orders = serializers.DecimalField(max_digits=5, decimal_places=2)
    avg_value = serializers.DecimalField(max_digits=5, decimal_places=2)


# API for customer analysis
class CustomerAnalysis(APIView):
    def get(self, request):
        start_date = request.data['start_date']
        end_date = request.data['end_date']

        orders = Orders.objects.filter(date__range=[start_date, end_date])
        customers = []
        total_orders = 0
        order_value = 0
        for order in orders:
            customers.append(order.customer_id)
            product = Products.objects.filter(product_id = order.product_id)
            order_value = product.unit_price * order.quantity
            total_orders +=1
        num_of_customer = len(set(customers))
        avg_value = order_value / total_orders

        data = [
            {
                "total_customers" : num_of_customer,
                "total_orders" :total_orders,
                "avg_value" : avg_value
            }
        ]

        serializer = DataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.data

        return Response(response_data, status=status.HTTP_200_OK)
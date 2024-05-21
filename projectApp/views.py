from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customers, Orders, Products
# from django.core import serializers

class DataSerializer(serializers.Serializer):
    total_customers = serializers.IntegerField()
    total_orders = serializers.IntegerField()
    avg_value = serializers.DecimalField(max_digits=20, decimal_places=2)


# API for customer analysis
class CustomerAnalysis(APIView):
    def get(self, request):
        print("API called")
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        try:
            orders = Orders.objects.filter(date_of_sale__range=[start_date, end_date])
            customers = []
            total_orders = 0
            order_value = 0
            for order in orders:
                customers.append(order.customer_id)
                print(order.product_id)
                order_value += order.product_id.unit_price * order.quantity
                total_orders +=1
            num_of_customer = len(set(customers))
            avg_value = order_value / total_orders

            data = {
                    "total_customers" : num_of_customer,
                    "total_orders" :total_orders,
                    "avg_value" : round(avg_value,2)
                }


            serializer = DataSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            response_data = serializer.data

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return  Response("Internal Sever Error", status = status.HTTP_500_INTERNAL_SERVER_ERROR)
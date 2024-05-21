# import_books.py
import csv
from datetime import datetime
from projectApp.models import Customers, Products, Orders

import os
import pytz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../Lumel.settings")


def run():
    file_path = 'data/orders.csv'
    with (open(file_path, 'r') as file):
        reader = csv.DictReader(file)
        for row in reader:
            cust = Customers(
                customer_id = row["Customer ID"],
                customer_name = row["Customer Name"],
                customer_email = row["Customer Email"],
                customer_address = row["Customer Address"],
            )
            prod = Products(
                product_id=row["Product ID"],
                product_name =row["Product Name"],
                unit_price = row["Unit Price"],
                region = row["Region"],
            )

            cust.save()
            prod.save()

            order = Orders.objects.get_or_create(
                order_id=row["Order ID"],
                product_id = prod,
                customer_id = cust,
                date_of_sale = datetime.strptime(row["Date of Sale"], "%d-%m-%Y"),
                quantity = row["Quantity Sold"],
                discount = row["Discount"],
                shipping_cost = row["Shipping Cost"],
                payment_method = row["Payment Method"],
            )



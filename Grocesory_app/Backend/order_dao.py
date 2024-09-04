# from sql_connection import get_sql_connection
# from datetime import datetime


# def insert_order(connection, order):
#     try:
#         cursor = connection.cursor()

#     #     # Insert order
#         order_query =( "INSERT INTO orders (customer_name, total_cost, datetime) VALUES (%s, %s, %s)")
#         order_data = (order['customer_name'], order['grand_total'], datetime.now())
#         cursor.execute(order_query,order_data)
#         connection.commit()

#         order_id = cursor.lastrowid

#         order_details_query = ( "INSERT INTO orders_details (order_id, product_id, quantity,total_price) VALUES (%s, %s, %s, %s)")


#         #Insert order details
#         order_details_data = []
#         for order_details_record in order['order_details']:
#             order_details_data.append([
#                 order_id,
#                 int(order_details_record['product_id']),
#                 float(order_details_record['quantity']),
#                 float(order_details_record['total_price']),
#             ])

#         cursor.executemany(order_details_query,order_details_data)
#         connection.commit()



#         return order_id
#     except Exception as e:
#         print(f"Error inserting product: {e}")
#         return None
    

# if __name__ == '__main__':
#     try:
#         connection = get_sql_connection()
#         print(insert_order(connection,{
#             'customer_name':'demo bhai ',
#             'total_cost':'120',
#             'order_details':[
#                 {
#                     'product_id':1,
#                     'quantity':2,
#                     'Total_price':60
#                 },
#                 {
#                     'product_id':2,
#                     'quantity':1,
#                     'Total_price':60
#                 }
#             ]
#         }))

#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         connection.close()  # Close the connection when done


# # from datetime import datetime
# # from sql_connection import get_sql_connection

# # def insert_order(connection, order):
# #     cursor = connection.cursor()

# #     order_query = ("INSERT INTO orders "
# #              "(customer_name, total_cost, datetime)"
# #              "VALUES (%s, %s, %s)")
# #     order_data = (order['customer_name'], order['total_cost'], datetime.now())

# #     cursor.execute(order_query, order_data)
# #     order_id = cursor.lastrowid

# #     order_details_query = ("INSERT INTO orders_details "
# #                            "(order_id, product_id, quantity, total_price)"
# #                            "VALUES (%s, %s, %s, %s)")

# #     order_details_data = []
# #     for order_detail_record in order['order_details']:
# #         order_details_data.append([
# #             order_id,
# #             int(order_detail_record['product_id']),
# #             float(order_detail_record['quantity']),
# #             float(order_detail_record['total_price'])
# #         ])
# #     cursor.executemany(order_details_query, order_details_data)

# #     connection.commit()

# #     return order_id

# # def get_order_details(connection, order_id):
# #     cursor = connection.cursor()

# #     query = "SELECT * from orders_details where order_id = %s"

# #     query = "SELECT order_details.order_id, order_details.quantity, orders_details.total_price, "\
# #             "products.name, products.price_per_unit FROM order_details LEFT JOIN products on " \
# #             "orders_details.product_id = products.product_id where orders_details.order_id = %s"

# #     data = (order_id, )

# #     cursor.execute(query, data)

# #     records = []
# #     for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
# #         records.append({
# #             'order_id': order_id,
# #             'quantity': quantity,
# #             'total_price': total_price,
# #             'product_name': product_name,
# #             'price_per_unit': price_per_unit
# #         })

# #     cursor.close()

# #     return records

# # def get_all_orders(connection):
# #     cursor = connection.cursor()
# #     query = ("SELECT * FROM orders")
# #     cursor.execute(query)
# #     response = []
# #     for (order_id, customer_name, total, dt) in cursor:
# #         response.append({
# #             'order_id': order_id,
# #             'customer_name': customer_name,
# #             'total': total,
# #             'datetime': dt,
# #         })

# #     cursor.close()

# #     # append order details in each order
# #     for record in response:
# #         record['orders_details'] = get_order_details(connection, record['order_id'])

# #     return response

# # if __name__ == '__main__':
# #     connection = get_sql_connection()
# #     # print(get_all_orders(connection))
# #     # print(get_order_details(connection,4))
# #     print(insert_order(connection, {
# #         'customer_name': 'dhaval',
# #         'total_cost': '500',
# #         'datetime': datetime.now(),
# #         'order_details': [
# #             {
# #                 'product_id': 1,
# #                 'quantity': 2,
# #                 'total_price': 50
# #             },
# #             {
# #                 'product_id': 3,
# #                 'quantity': 1,
# #                 'total_price': 30
# #             }
# #         ]
# #     }))







from sql_connection import get_sql_connection
from datetime import datetime

def insert_order(connection, order):
    try:
        cursor = connection.cursor()

        # Print the order data for debugging
        print("Order Data:", order)

        # Insert order
        order_query = "INSERT INTO orders (customer_name, total_cost, datetime) VALUES (%s, %s, %s)"
        order_data = (order['customer_name'], order['grand_total'], datetime.now())
        cursor.execute(order_query, order_data)
        connection.commit()

        order_id = cursor.lastrowid
        print("Inserted Order ID:", order_id)

        order_details_query = "INSERT INTO orders_details (order_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)"

        # Insert order details
        order_details_data = []
        for order_details_record in order['order_details']:
            order_details_data.append([
                order_id,
                int(order_details_record['product_id']),
                float(order_details_record['quantity']),
                float(order_details_record['total_price']),
            ])
        
        print("Order Details Data:", order_details_data)

        cursor.executemany(order_details_query, order_details_data)
        connection.commit()

        return order_id
    except Exception as e:
        print(f"Error inserting order: {e}")
        return None


# def get_order_details(connection, order_id):
#     cursor = connection.cursor()

#     query = "SELECT * from orders_details where order_id = %s"

#     query = "SELECT orders_details.order_id, orders_details.quantity, orders_details.total_price, "\
#             "products.name, products.price_per_unit FROM orders_details LEFT JOIN products on " \
#             "orders_details.product_id = products.product_id where orders_details.order_id = %s"

#     data = (order_id, )

#     cursor.execute(query, data)

#     records = []
#     for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
#         records.append({
#             'order_id': order_id,
#             'quantity': quantity,
#             'total_price': total_price,
#             'product_name': product_name,
#             'price_per_unit': price_per_unit
#         })

#     cursor.close()

#     return records

def get_order_details(connection, order_id):
    cursor = connection.cursor()

    query = "SELECT orders_details.order_id, orders_details.quantity, orders_details.total_price, "\
            "products.name, products.price_per_unit FROM orders_details LEFT JOIN products on " \
            "orders_details.product_id = products.products_id where orders_details.order_id = %s"

    data = (order_id, )

    cursor.execute(query, data)

    records = []
    for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price_per_unit': price_per_unit
        })

    cursor.close()

    return records



def get_all_order(connection):
    try:
        cursor = connection.cursor()

        # Insert order
        query = ("SELECT * FROM orders")
        cursor.execute(query)
        response = []
        for (order_id,customer_name,total,datetime) in cursor:
            response.append ({
                'order_id':order_id,
                'customer_name':customer_name,
                'total':total,
                'datetime':datetime
                })


        cursor.close()

        # append order details in each order
        for record in response:
            record['order_details'] = get_order_details(connection, record['order_id'])

        return response

    except Exception as e:
        print(f"Error inserting order: {e}")
        return None
    


if __name__ == '__main__':
    try:
        connection = get_sql_connection()
        # Test data
        # order = {
        #     'customer_name': 'John Doe',
        #     'grand_total': 100.0,
        #     'order_details': [
        #         {'product_id': 1, 'quantity': 2, 'total_price': 50.0},
        #         {'product_id': 2, 'quantity': 1, 'total_price': 50.0}
        #     ]
        # }
        # insert_order(connection, order)
        print(get_all_order(connection))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

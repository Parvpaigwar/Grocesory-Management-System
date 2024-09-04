from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = "SELECT products.products_id,products.name,products.um_id,products.price_per_unit ,uom.uom_name FROM products inner join uom on uom.uom_id=products.um_id"
    cursor.execute(query)
    response = []
    for (product_id,name,uom_id,price_per_unit,uom_name) in cursor:
        response.append({
            'product_id':product_id,
            'name':name,
            'uom_id':uom_id,
            'price_per_unit':price_per_unit,
            'uom_name':uom_name
        })

    return response


def insert_new_product(connection, product):
    try:
        cursor = connection.cursor()

        query = "INSERT INTO products (name, um_id, price_per_unit) VALUES (%s, %s, %s)"
        data = (product['product_name'],product['uom_id'],product['price_per_unit'])
        cursor.execute(query,data)
        connection.commit()

        return cursor.lastrowid
    except Exception as e:
        print(f"Error inserting product: {e}")
        return None
    
def delete_product(connection, product_id):
    try:
        cursor = connection.cursor()

        query = ("DELETE FROM products where products_id="+str(product_id))
        cursor.execute(query)
        connection.commit()

        return cursor.lastrowid
    except Exception as e:
        print(f"Error inserting product: {e}")
        return None

if __name__ == '__main__':
    try:
        connection = get_sql_connection()
        print(get_all_products(connection))

        # data = {'product_name':'Dove shampoo',
        #         'uom_id' : '1',
        #         'price_per_unit':65}
        # product_id = insert_new_product(connection, data)
        print(delete_product(connection,'10'))
        # if product_id:
        #     print(f"Product inserted with ID: {product_id}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()  # Close the connection when done

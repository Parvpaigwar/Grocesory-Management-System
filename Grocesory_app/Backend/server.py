from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import products_dao
import uom_dao
import json
import order_dao

app = Flask(__name__)

def get_db_connection():
    return get_sql_connection()

@app.route('/getproducts')
def get_all_products():
    try:
        connection = get_db_connection()
        products = products_dao.get_all_products(connection)
        response = jsonify(products)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.status_code = 500
        return response
    finally:
        if connection:
            connection.close()

@app.route('/getuoms',methods=['GET'])
def get_all_uoms():
    try:
        connection = get_db_connection()
        uoms = uom_dao.get_uoms(connection)
        response = jsonify(uoms)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.status_code = 500
        return response
    finally:
        if connection:
            connection.close()


@app.route('/insertproducts',methods=['POST'])
def insert_product():
    try:
        connection = get_db_connection()
        request_payload = json.loads(request.form['data'])
        product_id = products_dao.insert_new_product(connection,request_payload)
        response = jsonify({
            'product_id':product_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.status_code = 500
        return response
    finally:
        if connection:
            connection.close()


@app.route('/deleteproducts',methods=['POST'])
def delete_product():
    try:
        connection = get_db_connection()
        return_id = products_dao.delete_product(connection,request.form['product_id'])
        response = jsonify({
            'product_id':return_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.status_code = 500
        return response
    finally:
        if connection:
            connection.close()

@app.route('/insertorder',methods=['POST'])
def insert_order():
    try:
        connection = get_db_connection()
        request_payload = json.loads(request.form['data'])
        order_id = order_dao.insert_order(connection,request_payload)
        response = jsonify({
            'order_id':order_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.status_code = 500
        return response
    finally:
        if connection:
            connection.close()


@app.route('/getallorders',methods=['GET'])
def get_all_orders():
    try:
        connection = get_db_connection()
        orders = order_dao.get_all_order(connection)
        response = jsonify(orders)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.status_code = 500
        return response
    finally:
        if connection:
            connection.close()


# @app.route('/getorderdetails/<int:order_id>', methods=['GET'])
# def get_order_details_api(order_id):
#     try:
#         connection = get_db_connection()
#         order_details = order_dao.get_order_details(connection, order_id)
#         response = jsonify(order_details)
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response
#     except Exception as e:
#         response = jsonify({'error': str(e)})
#         response.status_code = 500
#         return response
#     finally:
#         if connection:
#             connection.close()


if __name__ == '__main__':
    print("Starting Python Server For Grocery Store Management System")
    app.run(port=5000)

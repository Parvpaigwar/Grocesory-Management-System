import mysql.connector

__cnx = None
def get_sql_connection():
    __cnx = mysql.connector.connect(user='root', password='parv9329',
                                host='127.0.0.1',
                                database='grocery_store_test') 
    return __cnx
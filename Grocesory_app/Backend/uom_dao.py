from sql_connection import get_sql_connection


def get_uoms(connection):
    cursor = connection.cursor()
    query = "SELECT * from uom"
    cursor.execute(query)
    response = []
    for (uom_id,uom_name) in cursor:
        response.append({
            'uom_id':uom_id,
            'uom_name':uom_name
        })

    return response



if __name__ == '__main__':
    try:
        connection = get_sql_connection()
        print(get_uoms(connection))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()  # Close the connection when done

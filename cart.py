from db import conn, cursor

def create_table_cart():
    query = """
        CREATE TABLE IF NOT EXISTS carts(
            id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            product_id INT NOT NULL
            );"""

    cursor.execute(query=query)
    
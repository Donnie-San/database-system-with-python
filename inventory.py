import mysql.connector

class InventoryManager:
    def __init__(self, host = "localhost", user = "root", passwd = "password", database = "ims_db"):
        self.__conn = mysql.connector.connect (
            host = host,
            user = user,
            passwd = passwd,
            database = database
        )

        self.__cursor = self.__conn.cursor()

    def add_product(self, product_name, category, stock_quantity, price):
        self.__cursor.execute("""
            INSERT INTO products (product_name, category, stock_quantity, price)
            VALUES (%s, %s, %s, %s);
        """, (product_name, category, stock_quantity, price))
        self.__conn.commit()

        print(f"{product_name} has been added successfully!")

    def update_stock(self, product_id, quantity, transaction_type):
        if transaction_type == "in":
            self.__cursor.execute("""
                UPDATE products
                SET stock_quantity = stock_quantity + %s
                WHERE product_id = %s;
            """, (quantity, product_id))
        else:
            self.__cursor.execute("""
                UPDATE products
                SET stock_quantity = stock_quantity - %s
                WHERE product_id = %s;
            """, (quantity, product_id))
        self.__conn.commit()

        print(f"Stock updated: {quantity} units {transaction_type.lower()}.")

        self.__cursor.execute("""
            INSERT INTO transactions (product_id, quantity, transaction_type)
            VALUES (%s, %s, %s);
        """, (product_id, quantity, transaction_type))
        self.__conn.commit()

        print(f"Added to transactions")

    def get_low_stock_items(self, threshold = 10):
        self.__cursor.execute("""
            SELECT * FROM products
            WHERE stock_quantity < %s;
        """, (threshold,))
        return self.__cursor.fetchall()

    def display_table(self, table):
        if table == "products":
            self.__cursor.execute("""
                SELECT * FROM products;
            """)
        else:
            self.__cursor.execute("""
                SELECT * FROM transactions;
            """)

        
        return self.__cursor.fetchall()

    def close_connection(self):
        self.__cursor.close()
        self.__conn.close()
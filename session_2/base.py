import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="session_2/orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def display_categories(db):
    query = '''
            SELECT category
            FROM products
            GROUP BY category
            '''
    cursor = db.execute(query)
    for category in cursor:
        print(category[0])

def number_of_customers(db):
    query = '''
            SELECT COUNT(customer_id)
            FROM customers
            '''
    cursor = db.execute(query)
    for category in cursor:
        print(f"{category[0]} customers")

def view_order_by_email(db):
    email = input("Enter email to display its orders: ")
    query = '''
            SELECT c.first_name, c.email, p.name, o.order_id
            FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id
            LEFT JOIN order_items oi ON o.order_id = oi.order_id
            LEFT JOIN products p ON oi.product_id = p.product_id
            WHERE c.email=?

            '''
    cursor = db.execute(query, (email,))
    for i in cursor:
        print(f"{i[0]} at {i[1]} ordered {i[2]} as part of order {i[3]}")

def under_two_bob(db):
    query = '''
            SELECT name
            FROM products
            WHERE price < 2.00
            '''
    cursor = db.execute(query)
    for category in cursor:
        print(category[0])

def top_BIG_SHOTS(db):
    query = '''
            SELECT c.first_name, SUM(p.price) AS total_spent, c.last_name
            FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id
            LEFT JOIN order_items oi ON o.order_id = oi.order_id
            LEFT JOIN products p ON oi.product_id = p.product_id
            GROUP BY c.customer_id
            ORDER BY total_spent DESC
            
            '''
    cursor = db.execute(query)
    for customer in cursor:
        if customer[1] == None:
            print(f"{customer[0]} {customer[2]} has spent a total of £0.00")
        else:
            print(f"{customer[0]} {customer[2]} has spent a total of £{customer[1]:.2f}")

def count_orders_per_category(db):
    query = '''
            SELECT p.category, COUNT(oi.order_id) AS total_orders
            FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id
            LEFT JOIN order_items oi ON o.order_id = oi.order_id
            LEFT JOIN products p ON oi.product_id = p.product_id
            GROUP BY p.category
            ORDER BY total_orders DESC
            
            '''
    cursor = db.execute(query)
    for category in cursor:
        if category[0] != None:
            print(f"{category[1]} orders have a product in the {category[0]} category")

    # Plot bar chart

def average_products_per_order(db):
    query = '''
            SELECT COUNT(p.product_id) AS total_products
            FROM customers c JOIN orders o ON c.customer_id = o.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            JOIN products p ON oi.product_id = p.product_id
            GROUP BY oi.order_id
            '''
    cursor = db.execute(query)
    total = 0
    count = 0
    for i in cursor:
        total += i[0]
        count += 1
    print(f"Average number of products per order: {total / count}")

def summarise_delivery_status(db):
    query = '''
            SELECT d.delivery_status, COUNT(d.delivery_status)
            FROM customers c JOIN orders o ON c.customer_id = o.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            JOIN products p ON oi.product_id = p.product_id
            JOIN deliveries d ON o.order_id = d.order_id
            GROUP BY d.delivery_status
            '''
    cursor = db.execute(query)
    for i in cursor:
        print(f"{i[1]} deliveries have status '{i[0]}'")

def menu():
    '''
    Prints menu and prompts for choice
    Returns choice (string)
    '''
    print("------------------------------")
    print("1 - Display product categories")
    print("2 - Display products under £2")
    print("3 - View order by email")
    print("4 - Display number of customers")
    print("5 - Display top spenders")
    print("6 - Count orders per product category")
    print("7 - Calculate average number of products per order")
    print("8 - Summarise deliveries by status")
    print("Q - quit")
    choice = -1
    while (choice not in ["1","2","3","4","5","6","7","8","Q"]):
        choice = input("Enter your choice: ").upper()
    print("------------------------------")
    return choice


def main():

    db = get_connection()

    while 1:
        choice = menu()
        match(choice):
            case "1":
                display_categories(db)

            case "2":
                under_two_bob(db)

            case "3":
                view_order_by_email(db)

            case "4":
                number_of_customers(db)
            
            case "5":
                top_BIG_SHOTS(db)

            case "6":
                count_orders_per_category(db)

            case "7":
                average_products_per_order(db)

            case "8":
                summarise_delivery_status(db)

            case "Q":
                exit()




    db.close()


if __name__=="__main__":
    main()

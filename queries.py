import sqlite3
conn = sqlite3.connect("orders.db")
cur = conn.cursor()

print("Customer orders (joined):")
for r in cur.execute("""SELECT c.name, o.amount FROM customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id"""):
    print(r)

print("\nTotal spend per customer:")
for r in cur.execute("""SELECT c.name, SUM(o.amount) AS total FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id ORDER BY total DESC"""):
    print(r)

conn.close()
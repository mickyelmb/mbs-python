import sqlite3

"""
1. Connect to a database
2. Create a cursor object
3. Write an SQL query
4. Commit changes to the database
5. Close the connection
"""
def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?, ?, ?)",(item, quantity, price))
    conn.commit()
    conn.close()



def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()


update(11,6,"Water Glass")
#delete("Wine Glass")
print(view())
#insert("Coffee Cup Glass", 10, 5)
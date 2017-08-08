import psycopg2

"""
1. Connect to a database
2. Create a cursor object
3. Write an SQL query
4. Commit changes to the database
5. Close the connection
"""
def create_table():
    conn=psycopg2.connect("dbname='TestDB' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='TestDB' user='postgres' password='postgres123' host='localhost' port='5432' ")
    cur=conn.cursor()
    # Bad practice vulnerable to SQL injection
    #cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" %(item, quantity, price))
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)",(item, quantity, price))
    conn.commit()
    conn.close()



def view():
    conn = psycopg2.connect("dbname='TestDB' user='postgres' password='postgres123' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='TestDB' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='TestDB' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

#create_table()
update(11,6,"Coffee Cup Glass")
#delete("Wine Glass")
print(view())
#insert("Wine Glass", 11, 4.5)
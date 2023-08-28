import sqlite3

# connect to database
conn = sqlite3.connect('customers.db')

# create a cursor
c = conn.cursor()

# insert a single record
c.execute("INSERT INTO customers VALUES (1,'John Doe', 'john_doe@email.com')")

# commit the changes
conn.commit()

# close the connection
conn.close()
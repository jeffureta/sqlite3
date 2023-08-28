import sqlite3

# connect to the database
conn = sqlite3.connect('customers.db')

# create  a table
c = conn.cursor()
c.execute('''CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# commit the changes
conn.commit()

#closes the connection
conn.close()
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (?,?,?)"

user = (1,'jose','asdf')
cursor.execute(insert_query,user)

users = [
    (2,'rolf','asdf'),
    (3,'ane','xyz')
]
cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
import mysql.connector

# username :  root
# password :  root
# host/ip  :  127.0.0.1
# databasename : python_db
# port : 3306
# Connecting from the server
conn = mysql.connector.connect(user='root',password='root',
                               host='localhost',
                               database='python_db',port=3306)
# create a cursor obj
cursor = conn.cursor()
#create or init a query
query_string = "CREATE TABLE Student(Name VARCHAR(255),Roll_no int);"

#execute query
cursor.execute(query_string);

print(conn)
# Disconnecting from the server
conn.close()

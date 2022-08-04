#pip install mysql-connector-python=8.0.17
#pip uninstall mysql-connector-python

import mysql.connector

# username :  root
# password :  root
# host/ip  :  127.0.0.1
# databasename : python_db
# port : 3306
# Connecting from the server

conn = mysql.connector.connect(user='root',password='root',
                               host='localhost',
                               database='python_community2',port=3306)
# create a cursor obj
cursor = conn.cursor()
#create or init a query
create_query_string = "CREATE TABLE Student(Name VARCHAR(255),Roll_no int unique);"
cursor.execute(create_query_string)
query_string = "insert into Student(Name,Roll_no) values(%s,%s)"
values = [('Ram','1234'),('Kasi','1234'),('Naga','2234')]

#execute query
# cursor.execute(query_string,values);   #to execeute single query
cursor.executemany(query_string,values); # to execute multiple queries
conn.commit()
# conn.rollback()

print(conn)
# Disconnecting from the server
conn.close()

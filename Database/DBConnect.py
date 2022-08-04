import mysql.connector

# username :  root
# password :  root
# host/ip  :  127.0.0.1
# databasename : python_community3
# port : 3306
try:
    # Connecting from the server
    conn = mysql.connector.connect(user='root',password='root',
                                   host='localhost',
                                   database='python_community3',port=3306)
    # create a cursor obj
    cursor = conn.cursor()
    #create or init a query
    #query_string = "CREATE TABLE customers_test(Name VARCHAR(255),Roll_no int);"
    query_string="desc customers_testsfasfae;"

    #execute query
    cursor.execute(query_string);

    myresult = cursor.fetchall()
    print(myresult)
except mysql.connector.DatabaseError as e:
    print("Currently we are facing some technical issues, please try after sometime")
# Disconnecting from the server
conn.close()
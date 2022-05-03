import mysql.connector

# connecting to the database
conn = mysql.connector.connect(user='root',password='root',
                               host='localhost',
                               database='python_community2',port=3306)

# preparing a cursor object
cursorObject = conn.cursor()

print("Displaying NAME and ROLL columns from the STUDENT table:")

# selecting query
query = "select * from python_community2.students"
cursorObject.execute(query)

myresult = cursorObject.fetchall()
print(myresult)
for x in myresult:
    print(x)

# disconnecting from server
conn.close()
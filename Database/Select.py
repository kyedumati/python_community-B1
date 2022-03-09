import mysql.connector

# connecting to the database
dataBase = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="pswrd",
    database="geeks")

# preparing a cursor object
cursorObject = dataBase.cursor()

print("Displaying NAME and ROLL columns from the STUDENT table:")

# selecting query
query = "SELECT NAME, ROLL FROM STUDENT"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()
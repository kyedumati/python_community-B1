import mysql.connector
import csv
from DBConnection import *
'''
Task: Export table data to csv file
Create a db connection
get table data
create a csv file
write table data to csv file
'''
CSV_FILE_PATH="C://Kasi/employee_data.xlsx"
try:
    #con=mysql.connector.connect(host='localhost',database='python_community3',user='root',password='root',port=3306)
    con= get_db_connection()
    cursor=con.cursor()
    cursor.execute("select * from employees_test")

    data=cursor.fetchall()
    print("data from db ",data)
    with open(CSV_FILE_PATH, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])  # write headers
        csv_writer.writerows(data)


    # for row in data:
    #      print("Employee Number:",row[0])
    #      print("Employee Name:",row[1])
    #      print("Employee Salary:",row[2])
    #      print("Employee Address:",row[3])
    #      print()
    #      print()
except mysql.connector.DatabaseError as e:
#except Exception as e:
     if con:
        con.rollback()
     print("There is a problem with sql :",e)
finally:
     if cursor:
        cursor.close()
     if con:
        con.close()


# Task
# Export database table data to csv/xlsx file
# Import csv file data to database table
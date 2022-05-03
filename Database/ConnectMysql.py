import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='python_community2',user='root',password='root',port=3306)
    cursor=con.cursor()
    cursor.execute("create table employees(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(10))")
    print("Table Created...")

    sql = "insert into employees(eno, ename, esal, eaddr) VALUES(%s, %s, %s, %s)"
    records=[(101,'Yuvraj',1000,'Mumbai'),
     (201,'Harbhajan',2000,'Ranchi'),
     (301,'Rohit',3000,'Delhi')]
    cursor.executemany(sql,records)
    con.commit()
    print("Records Inserted Successfully...")

    cursor.execute("select * from employees")
    data=cursor.fetchall()
    print("data from db ",data)
    for row in data:
         print("Employee Number:",row[0])
         print("Employee Name:",row[1])
         print("Employee Salary:",row[2])
         print("Employee Address:",row[3])
         print()
         print()
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


print("tests")


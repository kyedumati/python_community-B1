import mysql.connector

def get_db_connection():
    con = mysql.connector.connect(host='localhost', database='python_community3', user='root', password='root',
                                  port=3306)
    return con



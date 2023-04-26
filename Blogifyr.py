import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='password',database='blogging_platform')
if con.is_connected():
    print("Finally")

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()
mycursor.execute("show databases")  #execute method is used to run the query
for i in mycursor:
    print(i)

mycursor.execute("select * from a.emp1")
#for i in mycursor:
    #print(i)

result = mycursor.fetchall()
for i in result:
    print(i)

#result = mycursor.fetchone()
#print(result)
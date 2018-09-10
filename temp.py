import mysql.connector

database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='admin',
                                   database = 'mydb'
                                   )

mycursor = database.cursor()
#mycursor.execute("CREATE TABLE NEW (points INT,serial_number VARCHAR(255),violation_code VARCHAR(255),violation_description VARCHAR(255),violation_status VARCHAR(255)) ")

mycursor.execute("SHOW TABLES")
for i in mycursor:
    print (i)

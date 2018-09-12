# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:32:47 2018

@author: hmohan
"""

import mysql.connector

# CONNECTING TO DATABASE
database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='admin',
                                   database='mydb'
                                   )
#connect to cursor                       
cursor = database.cursor()

# table creation
#cursor.execute("CREATE TABLE previous_violations (name VARCHAR(255),address VARCHAR(255),zip_code VARCHAR(255),city VARCHAR(255)) ")

#query for inner join
sql = "SELECT \
    INSPECTIONS.facility_name as name, \
    INSPECTIONS.facility_address as address, \
    INSPECTIONS.facility_zip as zip_code, \
    INSPECTIONS.facility_city as city\
    FROM INSPECTIONS\
    INNER JOIN VIOLATIONS ON INSPECTIONS.serial_number=VIOLATIONS.serial_number"
   
'''   
cursor.execute(sql) 
myresult = cursor.fetchall()
for x in myresult:
    print (x)
'''
    
    
# insertion into table
    
cursor.execute(sql)
myresult = cursor.fetchall()
for i in range (0,len(myresult)):
    name = myresult[i][0]
    address = myresult[i][1]
    zip_code = myresult[i][2]
    city = myresult[i][3]
    query = "INSERT INTO previous_violations (name,address,zip_code,city) VALUES (%s,%s,%s,%s)"
    values = (name,address,zip_code,city)
    
    cursor.execute(query,values)
    database.commit()
    print('Inserted into table previous_violations')


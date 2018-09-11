# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:08:31 2018

@author: hmohan
"""
import mysql.connector
import xlrd
import os
os.chdir('/home/hmohan/Desktop')

book = xlrd.open_workbook('violations.xlsx')
sheet = book.sheet_by_name('violations')
#xl= pandas.ExcelFile('violations.xlsx')
# xls.sheet_names
#fd1 = xl.parse('violations')
database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='admin',
                                   database='mydb'
                                   )
cursor = database.cursor()
cursor.execute("CREATE TABLE VIOLATIONS (points VARCHAR(255),serial_number VARCHAR(255),violation_code VARCHAR(255),violation_description VARCHAR(255),violation_status VARCHAR(255))")
query = 'INSERT INTO VIOLATIONS (points,serial_number,violation_code,violation_description,violation_status) VALUES (%s,%s,%s,%s,%s)'                              
 
for r in range(1,sheet.nrows):
    points = sheet.cell(r,0).value
    serial_number = sheet.cell(r,1).value
    violation_code = sheet.cell(r,2).value
    violation_description = sheet.cell(r,3).value
    violation_status = sheet.cell(r,4).value
    
    values = [(points,serial_number,violation_code,violation_description,violation_status)]
    
    cursor.executemany(query,values)
    
#cursor.close()
#database.commit()
#database.close() 
    
book = xlrd.open_workbook('inspections.xlsx')
sheet = book.sheet_by_name('inspections')

cursor.execute("CREATE TABLE INSPECTIONS (activity_date VARCHAR(255),employee_id VARCHAR(255),facility_address VARCHAR(255),facility_city VARCHAR(255),facility_id VARCHAR(255),facility_name VARCHAR(255),facility_state VARCHAR(255),facility_zip VARCHAR(255),grade VARCHAR(255),owner_id VARCHAR(255),owner_name VARCHAR(255),pe_description VARCHAR(255),program_element_pe INT,program_name VARCHAR(255),program_status VARCHAR(255),record_id VARCHAR(255),score INT,serial_number VARCHAR(255),service_code INT,service_description VARCHAR(255))")
sql = '''INSERT INTO INSPECTIONS (activity_date,employee_id,facility_address,facility_city,facility_id,facility_name,facility_state,facility_zip,grade,owner_id,owner_name,pe_description,program_element_pe,program_name,program_status,record_id,score,serial_number,service_code,service_description) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
for r in range(1,sheet.nrows):
    activity_date = sheet.cell(r,0).value
    employee_id =sheet.cell(r,1).value
    facility_address = sheet.cell(r,2).value
    facility_city = sheet.cell(r,3).value
    facility_id = sheet.cell(r,4).value
    facility_name= sheet.cell(r,5).value
    facility_state = sheet.cell(r,6).value
    facility_zip = sheet.cell(r,7).value
    grade = sheet.cell(r,8).value
    owner_id = sheet.cell(r,9).value
    owner_name = sheet.cell(r,10).value
    pe_description = sheet.cell(r,11).value
    program_element_pe = sheet.cell(r,12).value
    program_name = sheet.cell(r,13).value
    program_status = sheet.cell(r,14).value
    record_id = sheet.cell(r,15).value
    score = sheet.cell(r,16).value
    serial_number = sheet.cell(r,17).value
    service_code = sheet.cell(r,18).value
    service_description = sheet.cell(r,19).value
    
    val =[(activity_date,employee_id,facility_address,facility_city,facility_id,facility_name,facility_state,facility_zip,grade,owner_id,owner_name,pe_description,program_element_pe,program_name,program_status,record_id,score,serial_number,service_code,service_description)]
    
    cursor.executemany(sql,val)

database.commit()

cursor.execute("SELECT * FROM VIOLATIONS")
myresult = cursor.fetchall()
for x in myresult:
    print(x)

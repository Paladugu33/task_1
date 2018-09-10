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
#fd1 = xl.parse('violations')
database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='admin',
                                   database='mydb'
                                   )
cursor = database.cursor()
query = '''INSERT INTO NEW (points,serial_number,violation_code,violation_description,violation_status)'''                               
 
for r in range(1,sheet.nrows):
    points = sheet.cell(r,0).value
    serial_number = sheet.cell(r,1).value
    violation_code = sheet.cell(r,2).value
    violation_description = sheet.cell(r,3).value
    violation_status = sheet.cell(r,4).value
    
    values = (points,serial_number,violation_code,violation_description,violation_status)
    
cursor.execute(query,values)
    
cursor.close()
database.commit()
database.close() 
                                  

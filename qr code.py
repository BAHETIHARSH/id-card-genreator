# # import EAN13 from barcode module
# from barcode import Code39
#
# # import ImageWriter to generate an image file
# from barcode.writer import ImageWriter
#
# # Make sure to pass the number as string
# number = 'harsh balaprasad baheti'
#
# # Now, let's create an object of EAN13 class and
# # pass the number with the ImageWriter() as the
# # writer
# my_code = Code39(number, writer=ImageWriter())
#
# # Our barcode is ready. Let's save it.
# my_code.save("Barcodes/new_code1")

# import pandas as pd
# data=pd.read_excel("./data_files.xlsx")
# import xlrd
# workbook = xlrd.open_workbook("data_files.xlsx")
# sheet=workbook.sheet_by_index(0)
# print(sheet.cell_value(0,0))
# importing the module
# import sqlite3
#
# # creating an connection
# conn = sqlite3.connect("tutorialspoint.db") # db - database
#
# # Cursor object
# cursor = conn.cursor()
#
# import sqlite3
#
# # creating an connection
# conn = sqlite3.connect("tutorialspoint.db") # db - database
#
# # Cursor object
# cursor = conn.cursor()
#
# fetch_students_sql = """
# SELECT * FROM databases;
# """
#
# # executing the SQL query
# cursor.execute(fetch_students_sql)
# # inserting data into the students table
# # for i in range(10):
# # insert_student_one_sql = """INSERT INTO databases VALUES ("10", "John Hill", "cse","22/09/2001","B+","photo.jpg");"""
# # cursor.execute(insert_student_one_sql)
# students = cursor.fetchall()
# print(students[0])
# conn.commit()
#
# conn.close()

import csv
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["Name"])





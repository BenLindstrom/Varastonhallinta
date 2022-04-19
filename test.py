from django.db import connection
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'localhost\sqlexpress'
database = 'SampleDB' 
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLEXPRESS;DATABASE=SampleDB;Trusted_Connection=yes;')
cursor = connection.cursor()

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()
    
cursor.close()
connection.close()
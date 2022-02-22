from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import pyodbc

server = 'vnetpoc321.database.windows.net'
database = 'mydb'
username = 'admin321'
password = 'Ragh@db31'
driver = '{ODBC Driver 17 for SQL Server}'


cnxn = pyodbc.connect('DRIVER=' + driver +
                      ';SERVER=' + server +
                      ';DATABASE=' + database +
                      ';UID=' + username +
                      ';PWD=' + password)

app = Flask(__name__)

# #Here I used Private IP To test the things 
# app.config['MYSQL_HOST'] = '10.0.1.4'
# app.config['MYSQL_USER'] = 'admin'
# app.config['MYSQL_PASSWORD'] = 'admin'
# app.config['MYSQL_DB'] = 'mydb'
 
# mysql = MySQL(app)

@app.route("/")
def index():
    return "Hello World"

@app.route("/getdata")
def getdata():
    cursor = cnxn.cursor()
    print('Connection established')
    cursor.execute("select * from MyUsers;")
    data=cursor.fetchall()
    print(data)
    return str(data)

#     #Creating a connection cursor
#     cursor = mysql.connection.cursor()
#     cursor.execute("select * from mydb.MyUsers;")
#     data = cursor.fetchall()
#     print(data)
#     return str(data)

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()

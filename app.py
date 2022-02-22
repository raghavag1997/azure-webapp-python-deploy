from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#Here I used Private IP To test the things 
app.config['MYSQL_HOST'] = 'vnetpoc321.database.windows.net''
app.config['MYSQL_USER'] = 'admin321'
app.config['MYSQL_PASSWORD'] = 'Ragh@db31'
app.config['MYSQL_DB'] = 'mydb'
 
mysql = MySQL(app)

@app.route("/")
def index():
    return "Hello World"

@app.route("/getdata")
def getdata():
    #Creating a connection cursor
    cursor = mysql.connection.cursor()
    cursor.execute("select * from MyUsers;")
    data = cursor.fetchall()
    print(data)
    return str(data)

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()

# from flask import Flask, render_template
# app= Flask(__name__)


# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__=="__main__":
#     app.run()
import re
import textwrap
import pyodbc
from flask import Flask,request, render_template
app= Flask(__name__)




# @app.route("/")
# def home():
#     return render_template("index.html")


driver = '{ODBC Driver 17 for SQL Server}'

server_name = 'samplecode2server'
database_name = 'samplecode2'

server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)

username = "samplecode2admin"
password = "Spring@2021"

connection_string = textwrap.dedent('''
    Driver={driver};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
'''.format(
    driver=driver,
    server=server,
    database=database_name,
    username=username,
    password=password
))

@app.route('/')
def index():
    return render_template('index.html')


    


# li=str((result[0][0]))
# print(li)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return (a)


cnxx: pyodbc.Connection = pyodbc.connect(connection_string)
crsr: pyodbc.Cursor = cnxx.cursor()
select_sql = "SELECT Name,Picture FROM dbo.names where Room = '550';"
crsr.execute(select_sql)
result=(crsr.fetchall())
a=''
print(str(result))
for i in result:
    a= a + str(i)

print(a)
cnxx.close()

if __name__=="__main__":
    app.run()

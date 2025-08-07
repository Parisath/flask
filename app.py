from flask import Flask,render_template,redirect,url_for,request
import sqlite3 as sql
import mysql.connector
import pymysql
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
# @app.route("/")
# def home():
#     # return "<h1>hello home page</h1>"
#     return render_template("./home.html")
# @app.route("/contact")
# def contact():
#     # return "<h1>welcome contact page</h1>"
#     return render_template("./contact.html")

# @app.route("/contact/account")
# def account():
#     return "<h1>welcome to account page</h1>"
# @app.route("/login/<name>/<int:age>")
# def login(name,age):
#     if age>=18:
#         return redirect(url_for("home"))    
#     else:
#         return redirect(url_for("contact"))
    
# @app.route("/call")
# def call():
#     name="john"
#     return render_template("jinga.html",name=name)

# @app.route("/variable")
# def variable():
#     name="john"
#     return redirect(url_for("call",name=name))
# @app.route("/admin/<name>")
# def admin(name):
#     return f"<h1>admin page{name}</h1>"
# @app.route("/programmer/<name>")
# def programmer(name):
#     return f"<h1>welcome to programmer{name}</h1>"
# @app.route("/manager/<name>")
# def manager(name):
#     return f"<h1>welcome to manager{name}</h1>"
# @app.route("/input/<roll>/<name>")
# def input(name,roll):
#     if roll=="admin":
#         return redirect(url_for("admin",name=name))
#     elif roll=="programmer":
#         return redirect(url_for("programmer",name=name))
#     elif roll=="manager":
#         return redirect(url_for("manager",name=name))
#     else:
#         return "<h1>invalid input</h1>" 
# @app.route("/database")
# def student():
#     student={
#          "1":{
#              "tamil":80,
#             "english":70,
#              "maths":60,
#             "social":80,
#              "science":80,
#     }
# }
#     return render_template("flow_control.html",student=student)
# @app.route("/calculator/<int:num1>/<int:num2>")
# def calculator(num1,num2):
#     return render_template("calculator.html",num1=num1,num2=num2)
# @app.route("/sub/<int:num1>/<int:num2>")
# def sub(num1,num2):
#     return f"{num1-num2}"

# @app.route("/homes")
# def homes():
#     return render_template("homes.html")
# @app.route("/contactus")
# def contactus():
#     return render_template("contactus.html")
# @app.route("/aboutus")
# def aboutus():
#     return render_template("aboutus.html")
# @app.route("/op/<int:num1>/<int:num2>")
# def ran(num1,num2):
#     return render_template("og.html",num1=num1,num2=num2)
# @app.route('/')
# def form():
#     return render_template("register.html")
# @app.route("/logins",methods=['post'])
# def logins():
#     name=request.form.get("username") 
#     password=request.form.get("password")
#     email=request.form.get("email")
#     if not name or not password or not email:
#         return f"all values are required"
#     if len(name)<=3:
#          return f"your value must be three character"
#     if len(password)<=3:
#          return f"the password must be three character"
#     if "@" not in email or "." not in email:
#          return f"enter the valid email"
#     return render_template("logins.html")
# @app.route("/home",methods=["POST"])
# def home():
#     name=request.form.get("username")
#     if len(name)<=3:
#         return f"the value must be 4 character otherwise you do not login the home page"
#     return render_template("home.html",name=name)
# @app.route("/home")
# def home():
#     return render_template("login.html")
# @app.route("/")
# def index():
#     return render_template("login_sql.html")

# @app.route("/index",methods=["post"])
# def home():
#     name=request.form.get("username")
#     password=request.form.get("password")
#     conn=sql.connect("sql_db.db")
#     cur=conn.cursor()
#     cur.row_factory=sql.Row #used to select the specify rows and columns
#     cur.execute("insert into student(name,password)values(?,?)",(name,password))
#     cur.execute("select * from student") 
#     rows=cur.fetchall() #take the data
#     conn.commit() #save the data
#     conn.close() #close the database

    # conn=sql.connect("sql_db.db")
    # cur=conn.cursor()
    # cur.execute("insert into student(name,password)values(?,?)",(name,password))
    # cur.execute("select * from student")
    # rows=cur.fetchall()
    # conn.commit()
    # conn.close()

    # conn=sql.connect("sql_db.db")
    # cur=conn.cursor()
    # cur.execute("insert into student(name,password)values(?,?)",(name,password))
    # cur.execute("select * from student")
    # rows=cur.fetchall()
    # conn.commit()
    # conn.close()
    # return render_template("index.html",rows=rows)



# @app.route("/")
# def lay():
#     con=sql.connect("sql_db.db")
#     con.row_factory=sql.Row   
#     cur=con.cursor()
#     cur.execute("select * from user")
#     data=cur.fetchall()
#     con.commit()
#     return render_template("lay.html",data=data)

# @app.route("/get")
# def get():
#     return render_template("add_user.html")

# @app.route("/add",methods=["POST"])
# def add():
#     if request.method=="POST":
#         name=request.form.get('username')
#         email=request.form.get("email")
#         con=sql.connect("sql_db.db")
#         con.row_factory=sql.Row
#         cur=con.cursor()
#         cur.execute("insert into user(usename,email) values(?,?)",(name,email))
#         con.commit()
#         # con.close()
#     return redirect("/")





# @app.route("/edit/<int:id>",methods=["GET","POST"])
# def edit(id):
#     name=request.form.get('username')
#     email=request.form.get("email")
#     con=sql.connect("sql_db.db")
#     con.row_factory=sql.Row
#     cur=con.cursor()
#     cur.execute("select * from user where uid=?",(id,))
#     data=cur.fetchone()
#     con.commit()
#     return render_template("edit.html",data=data)


# @app.route("/update/<id>",methods=["POST"])
# def update(id):
#     name=request.form.get('username')
#     email=request.form.get("email")9
#     con=sql.connect("sql_db.db")
#     con.row_factory=sql.Row
#     cur=con.cursor()
#     cur.execute("UPDATE  user set  usename=?,email=? where uid=?",(name,email,id))
#     data=cur.fetchone()
#     con.commit()
#     return redirect("/")




# @app.route("/delete/<id>")
# def delete(id):
#     con=sql.connect("sql_db.db")
#     con.row_factory=sql.Row
#     cur=con.cursor()
#     cur.execute("delete from user where uid=?",(id,))
#     con.commit()
#     return redirect("/")

# @app.route("/")
# def stud():
#     return render_template("tab.html")
# @app.route("/")
# def registers():
#     return render_template("registers.html")
# @app.route("/op",methods=["POST"])
# def op():
#     if request.method=="POST":
#         password=request.form.get("password")
#         confirm=request.form.get("confirm password")
#         if password==confirm:
#             return render_template("lo.html")
#         else:
#             return f"your password is not correct check"
# @app.route("/ho",methods=["POST"])
# def ho():
#     return "<h1>you are login</h1>"

#mysql
# @app.route("/")
# def table():
#     conn=pymysql.connect(
#         host="localhost",
#         user="root",
#         password="12345",
#         database="kumarss"
#     )
#     cur=conn.cursor()
#     cur.execute("create table if not exists students(id int auto_increment primary key,name varchar(100))")
#     conn.commit()
#     conn.close()
#     return render_template("add.html")
# @app.route("/add",methods=["POST"])
# def add():
#     name=request.form.get("name")
#     conn=pymysql.connect(
#         host="localhost",
#         user="root",
#         password="12345",
#         database="kumarss"
#     )

#     cur=conn.cursor()
#     cur.execute("insert into students(name)values(%s)",(name,))
#     conn.commit()
#     conn.close()
#     return "data added"

#  SQLALCHEMY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #Give The location of the database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #disable the warning

# db=SQLAlchemy(app)
# #intialize the table and column
# class User(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String)
#     email = db.Column(db.String)

# create the table and column here
# with app.app_context():
#     db.create_all()
# #insert the data
# user=User(name="john",email="parisath213@gmail.com")
# db.session.add(user)
# db.session.commit()

# #this is confirmation message
# print("table created")

#
# import os
# basedir=os.path.abspath(os.path.dirname(__file__))
# db_path=os.path.join(basedir,"sql_db.db")
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #Give The location of the database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disabling the warnings

# db=SQLAlchemy(app) 

# #Initialize the table and column here
# class Userss(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     email = db.Column(db.String)

# #create the table and column here
# with app.app_context():
#     db.create_all()
    
#     #insert the data here
#     user = Userss(name="John",email="John@gmail.com") 
#     db.session.add(user)
#     db.session.commit()
#     print("Table created and user add successfully...")
  



# @app.route("/a/<int:a>")
# def run(a):
#     return render_template("home.html",a=a)

if __name__=="__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0',port=7000)


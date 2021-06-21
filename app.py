from flask import Flask, render_template, redirect, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="yout_host",
  user="your_user",
  password="your_password",
  database="your_database",
  auth_plugin='your_auth_plugin'
)

db = mydb.cursor() 


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
    firstname = request.form.get("firstname")
    if not firstname:
        return render_template("error.html", message="Missing firstname")

    lastname = request.form.get("lastname")
    if not lastname:
        return render_template("error.html", message="Missing lastname")

    email = request.form.get("email")
    if not email:
        return render_template("error.txt", message="Invalid email")

    #Database to store the data of the new guests
    sql = "INSERT INTO MyGuests (firstname, lastname, email) VALUES (%s, %s, %s)"
    val = (firstname, lastname, email)
    db.execute(sql, val)
    mydb.commit()

    return redirect("/guests")    

@app.route("/guests", methods=["POST", "GET"])
def guests():
  db.execute("SELECT * FROM MyGuests")
  row = db.fetchall()
  
  return render_template("guests.html", guests=row)

 

from flask import Flask, render_template, request, redirect, url_for, session 
from auth import verify_master_password
app = Flask(__name__)
app.secret_key = "supersecretpass1234"
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method=='POST':
        password = request.form.get('password')
        result=verify_master_password(password)
        if result:
            session["Logged_in"]=True
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))
    return render_template("login.html")
from flask import Flask, render_template, request, redirect, url_for, session 
from auth import verify_master_password
from vault import add_password, get_password
from generate_password import generate_password, check_strength
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
            return render_template("login.html", error="Wrong password!")
    return render_template("login.html")
@app.route("/home")
def home():
    if not session.get("Logged_in"):
        return redirect(url_for("login"))
    return render_template("home.html")
@app.route("/add_password", methods=['GET','POST'])
def add_password_page():
    if request.method=='POST':
        password = request.form.get('password')
        site = request.form.get('site')
        add_password(site, password)
        return redirect(url_for("home"))
    return render_template("add_password.html")
@app.route("/get_password", methods=['GET','POST'])
def get_password_page():
    if request.method=='POST':
        site=request.form.get('site')
        result=get_password(site)
        return render_template("get_password.html", password=result)
    return render_template("get_password.html")
@app.route("/generate_password")
def generate():
    return render_template("generate.html", password=generate_password())
@app.route("/password_strength", methods=['GET','POST'])
def check_password_strength():
    result=None
    if request.method=='POST':
        password=request.form.get('password')
        result=check_strength(password)
    return render_template("password_strength.html", strength=result)
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)

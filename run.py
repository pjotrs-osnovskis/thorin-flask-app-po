import os

import json
# Import Flask class
from flask import Flask, render_template, request, flash
# Creating an instance of it and storing in a variable

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Index route 
@app.route("/")
def index():
    return render_template("index.html")


# About route 
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

# Members route to show every member in separate pages
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)

# Contact route 
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


# Careers route 
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")



# Live Preview
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # Never have debug=True in deployment, mainly for security reasons
        debug=False
    )
import os

import json
#Import Flask class
from flask import Flask, render_template
# Creating an instance of it and storing in a variable
app = Flask(__name__)


# Index route decorator
@app.route("/")
def index():
    return render_template("index.html")


# About route decorator
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


# Contact route decorator
@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


# Careers route decorator
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")



# Live Preview
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # Never have debug=True in deployment, mainly for security reasons
        debug=True
    )
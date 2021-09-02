import os
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
    return render_template("about.html")

# Contact route decorator
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Thing to tun a server (as I understand at this point)
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # Never have debug=True in deployment, mainly for security reasons
        debug=True
    )
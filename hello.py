from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Index!"
 
@app.route("/hello")
def hello():
    return "Hello World!"
 
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name

@app.route("/signup")
def signup():
    return render_template("signup.html")

 
if __name__ == "__main__":
    app.run()
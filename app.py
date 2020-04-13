from flask import Flask, render_template, request, session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    headline="From app.py"
    return render_template("index.html", headline=headline)

@app.route("/names")
def names():
    names=["Jacob", "Elsa", "Jotham"]
    return render_template("names.html",names=names)

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

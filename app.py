from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_h():
    return render_template("index.j2")

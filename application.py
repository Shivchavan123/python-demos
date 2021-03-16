import random
from flask import Flask, render_template, request


app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/hello")
def me():
    name=request.args.get("uname")
    if not name:
        return render_template("failure.html")
    return render_template("helloo.html", ame=name)   


if __name__=="__main__":
    app.run(debug=True)

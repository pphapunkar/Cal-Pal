from flask import Flask, render_template, request, redirect, abort, jsonify

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/Events")
def events():
    return render_template("Events.html")


@app.route("/create")
def createvent():
    return render_template("create.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

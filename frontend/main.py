from flask import Flask, render_template, request, redirect, abort, jsonify

URL = 'https://backend-dot-cal-pal-250416.appspot.com/Events'

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/Events")
def events():
    data = request.get(URL + '/Events')
    print(data)
    return render_template("Events.html")


@app.route("/create", methods=['POST'])
def createvent():
    url = URL + '/create'
    data = request.form.to_dict(flat=True)
    print(request.post(url, data=data))
    return render_template("create.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
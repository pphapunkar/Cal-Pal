from flask import Flask, render_template, request, redirect, abort, jsonify
import requests
import uuid
URL = 'https://backend-dot-cal-pal-250416.appspot.com/Events'

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/Events")
def events():
    data = request.get(URL)
    print(data)
    return render_template("Events.html")
@app.route("/addEvents")  
def addEvent():
    return render_template("create.html")

@app.route("/Events/create", methods = ['POST'])
def createvent():
    print('URL--' + URL)
    url = URL + '/create/' +str(uuid.uuid4())
    print('Passed URL' + url)
    data = request.form.to_dict(flat=True)
    print(data)
    requests.post(url, data=data)
    print(requests.post(url, data=data))
    return redirect('/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
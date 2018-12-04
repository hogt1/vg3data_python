from datetime import datetime
from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

# Replace the existing home function with the one below
@app.route("/")
def index():
    return render_template("index.html")

# Her er <name> et parameter til ruten eks.:http://127.0.0.1/hello/tom
@app.route("/hello/<name>")
def hello(name):
    now = datetime.now()
    content = "Hello there, {} {:%d.%m.%Y %H:%M:%S}".format(name, now)
    return render_template(
        "hello.html",
        title='Hello, Flask',
        content=content,
        date=datetime.now(),
        name=name
    )

# Ofte vil du servere filer 
@app.route("/documents/<filename>")
def get_document(filename):
    return send_from_directory('uploads', filename, as_attachment=True)

# New functions
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/form/post", methods=['POST'])
def form_post():
    #stack = rpn.calculate(request.form['stack'], request.form['op'])
    #for k, v in request.environ.items():
    #    print('{}={}'.format(k,v))
    return '<pre>Fornavn: {}\nEtternavn: {}\nDato:{}</pre>'.format(
        request.form['firstname'], 
        request.form['lastname'], 
        request.form['dato'])


@app.route("/kalkulator")
def kalkulator():
    return render_template('kalkulator.html')

# Motta JSON Data
# Test med et script 
# import requests
# response = requests.post('http://localhost:5000/api/add_data', json={'some_value_1':123, 'some_value_2':234})
@app.route("/api/add_data", methods=['POST'])
def add_data():
    data = request.json
    for k, v in data.items():
        print('{}={}'.format(k,v))

    return "Data OK?"

# Returnerer data i json format - eks. en sensor
@app.route("/api/dht11")
def dht11():
    data = {'temperature':25, 'humidity': 21}

    # jsonify tar seg av både mimetype og json.dumps
    return jsonify(data)
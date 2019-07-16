from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return "Hello World! Python works but auto reload doesnt"


@app.route('/values', methods=['POST', 'GET'])
def values():
    if request.method == "POST":
        international_flight = float(request.form['internationalFlight']) * 0.10
        domestic_flight = float(request.form['domesticFlight']) * 0.12
        train = float(request.form['train']) * 0.01
        bus = float(request.form['bus']) * 0.02
        car = float(request.form['car']) * 0.19
        total = international_flight + domestic_flight + train + bus + car
    return jsonify(total)


if __name__ == "__main__":
    app.run(debug=True)

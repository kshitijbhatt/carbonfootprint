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
        co2 = float(total)
        atree_offset = 22
        atree_life = 20
        offset = int(round(co2 / atree_offset / atree_life))
        atree_survive = 80
        total_trees = int(round(offset * 100 / atree_survive))
        atree_cost = 300
        total_cost = int(round(total_trees * atree_cost))

        data = {
            "co2": co2,
            "offset": offset,
            "num_trees": total_trees,
            "tree_cost": atree_cost,
            "total_cost": total_cost
        }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

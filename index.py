from flask import Flask, request, jsonify, redirect, url_for, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == "POST":
        international_flight = float(request.form['internationalFlight']) * 0.10
        domestic_flight = float(request.form['domesticFlight']) * 0.12
        train = float(request.form['train']) * 0.01
        bus = float(request.form['bus']) * 0.02
        car = float(request.form['car']) * 0.19
        total = international_flight + domestic_flight + train + bus + car
        co2 = float(total)
        absorption_rate = 22
        life_of_tree = 20
        survival_rate = 80
        cost_per_tree = 300
        total_offset = (co2 / absorption_rate) / life_of_tree
        total_trees = int(round(total_offset * 100 / survival_rate))
        total_cost = int(total_trees * cost_per_tree)
        data = [{
            "totalEmission": total_offset,
            "noOfTrees": total_trees,
            "totalCost": total_cost
        }]
        # return render_template('results.html', data=data)
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

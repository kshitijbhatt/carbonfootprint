from flask import Flask, escape, request,json
app = Flask(__name__)


@app.route('/')
def index():
    co2 = int(request.args.get("co2"))
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
    data = json.dumps(data)
    return str(data)


if __name__ == "__main__":
    app.run(debug=True)

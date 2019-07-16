from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return "Hello World! Python works but auto reload doesnt"


@app.route('/flight/domestic<name>')
def hello_name(name):
    return 'Hello %s!' % name


if __name__ == "__main__":
    app.run(debug=True)

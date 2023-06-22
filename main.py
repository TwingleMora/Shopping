from flask import Flask, render_template, jsonify

print(__name__)

app = Flask(__name__)
ITEMS = [{
  'name': "Apple",
  'price': 12
}, {
  'name': "Car",
  'price': 25
}, {
  'name': "Jacket",
  'price': 32
}]


@app.route("/")
def hello_world():
  return render_template('main.html', items=ITEMS)


@app.route("/api/items")
def list_items():
  return jsonify(ITEMS)


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)

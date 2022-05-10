from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

mongo = MongoClient("mongodb://smartGrid:smartGrid12345@127.0.0.1")


@app.route('/')
def super_endpoint():
    elements = mongo.smart_grid.test.find({})
    result = ''
    for element in elements:
        result += element['test']
    return render_template("home.html")

@app.route('/test', methods=['POST'])
def test():
    test_data = {
        "test": "test"
    }
    mongo.smart_grid.test.insert_one(test_data)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
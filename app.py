# Imports
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import pymongo
from flask import Flask, jsonify
import io
import json
from bson import ObjectId
from flask.json import JSONEncoder

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sp500"]

mycol = mydb["stock"]

@app.route("/")
def test():
    inventory = list(mycol.find())
    # print("====================")
    # # print(inventory)
    # print("====================")

    
    class JSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, ObjectId):
                return str(o)
            return json.JSONEncoder.default(self, o)
    # print("====================")

    inventory = JSONEncoder().encode(inventory)
    # print(inventory)
    # print(type(inventory))

    # print("====================")

    x = json.loads(inventory)
    # print(x)
    # print(type(x))
    # print(x[0])
    # print(type(x[0]))


    with open('stock.json', 'w') as json_file:
        json.dump(x, json_file)

    return jsonify(inventory)

test()

print("----------------")
print("Successful!")
print("----------------")


if __name__ == "__main__":
    app.run(debug=True)


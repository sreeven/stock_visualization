from flask import Flask
from flask_pymongo import PyMongo
import load_data

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/stocks"
mongo = PyMongo(app)

values = load_data.data()

stocks.insert_many(values)




# @app.route("/")
# def home_page():
#     online_users = mongo.db.users.find({"online": True})
#     return render_template("index.html",
#         online_users=online_users)
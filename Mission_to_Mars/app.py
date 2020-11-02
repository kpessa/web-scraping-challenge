from flask import Flask, render_template, url_for, redirect, flash
from scrape_mars import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    dict = scrape_function()
    mongo.db.mars.replace_one({}, dict, upsert=True)
    return "Website(s) successfully scraped"


if __name__ == "__main__":
    app.run(debug=True)

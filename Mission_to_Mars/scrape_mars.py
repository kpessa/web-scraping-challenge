from flask import Flask
from scrape import *

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"

@app.route("/scrape")
def scrape():
    dict = scrape_function()
    return dict

if __name__ == "__main__":
    app.run(debug=True)


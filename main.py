import pandas
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") #decarator, it connect below method to this function
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>") #decarator, it connect below method to this function
def about(station, date):
    df = pandas.read_csv("")
    temperature = df.station(date)
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


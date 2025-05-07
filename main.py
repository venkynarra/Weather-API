from flask import Flask, render_template

app = Flask("website")

@app.route("/home") #decarator, it connect below method to this function
def home():
    return render_template("tutorial.html")
@app.route("/about/") #decarator, it connect below method to this function
def about():
    return render_template("about.html")
app.run(debug=True)
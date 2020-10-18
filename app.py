from flask import Flask,request,render_template
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/')
@cross_origin()
def home():
    return render_template("home.html",text="Hey! Guys - This is PAAS example")


if __name__ == "__main__":
    app.run(debug=True)
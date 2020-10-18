from flask import Flask,request,render_template
from flask_cors import cross_origin
import os

app = Flask(__name__)


@app.route('/')
@cross_origin()
def home():
    return render_template("home.html",text="Hey! Guys - This is PAAS example")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask,request,render_template
from flask_cors import cross_origin
import os
import pickle
import warnings
import time
warnings.filterwarnings("ignore")

app = Flask(__name__)


@app.route('/')
@cross_origin()
def home():
    return render_template("home.html")

@app.route('/user_data',methods = ["GET", "POST"])
def post():
    if request.method == "POST":
        f1 = float(request.form['f1'])
        f2 = float(request.form['f2'])
        f3 = float(request.form['f3'])
        f4 = float(request.form['f4'])
        f5 = float(request.form['f5'])
        f6 = float(request.form['f6'])
        inputs = [f1,f2,f3,f4,f5,f6]
        time.sleep(3)
        model = pickle.load(open('model.pkl','rb'))

        predict = model.predict([inputs])
     
    return render_template("home.html",text=predict[0])

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

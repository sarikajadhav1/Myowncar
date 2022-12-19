from flask import Flask , jsonify,render_template,request,redirect,url_for
from utils import CarPrice
import config
import numpy as np
import pandas as pd
import sklearn

app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("Welcome to Car price prediction")
    return render_template("home.html")

@app.route("/car_price",methods = ["GET","POST"])

def prediction():
    
    if request.method == "POST":
        print("We are in Post method")
    
        data = request.form
        print("Data :",data)

        year     = int(request.form["year"])
        mileage  = int(request.form["mileage"])
        hp       = int(request.form["hp"])
        gear     = request.form["gear"]
        fuel     = request.form["fuel"]
        make     = request.form["make"]

        car_price = CarPrice(data)
        price = car_price.get_pred_price()
        
        if price < 0:
            price = "Please enter valit inputs"

        # return jsonify({"Price": np.round(price)})
        return render_template("home.html",prediction = np.round(price))
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)
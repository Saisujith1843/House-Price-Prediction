from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict', methods=['POST'])
def predict():
        Bedrooms = float(request.form['Bedrooms'])
        Bathrooms = float(request.form['Bathrooms'])
        Sqft_living = float(request.form['Sqft_living'])
        Sqft_lot = float(request.form['Sqft_lot'])
        Floors = float(request.form['Floors'])
        Grade = float(request.form['Grade'])
        Sqft_basement = float(request.form['Sqft_basement'])
        Number_of_Years = float(request.form['Number_of_Years'])
        prediction = model.predict([[Bedrooms, Bathrooms, Sqft_living, Sqft_lot, Floors, Grade,Sqft_basement, Number_of_Years]])
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text="The house price based on the neccesity is: {}".format(output))

    if __name__=="__main__":
    app.run(debug=True)
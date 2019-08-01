# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, render_template, request, jsonify
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, StandardScaler
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('./model/model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        # [('name', 'abs'), ('R&D', '12345'), ('admin', '23456'), ('marketing', '321456'), ('location', 'NewYork')]
        #data = request.get_json(force=True)
        print(request.form)
        #print(request.form['gender'])
        #gender=0
        #if request.form['gender']=="male":
                #gender= 1
        print(request.form["name"])
        print(request.form["R&D"])
       # data = np.reshape(data, (1,-1))
        

        # Encoding categorical data
        # from sklearn.preprocessing import LabelEncoder, OneHotEncoder
        # labelencoder = LabelEncoder()
        # location = labelencoder.fit_transform(request.form["location"]])
        stats2 = {
                "California":0,
                "NewYork":2,
                "Florida":1
        }
        stats3 = {
                0:"California",
                1:"Florida",
                2:"NewYork"
        }
        location = stats2[request.form["location"]]
        # location = labelencoder.fit_transform(stats)

        # data = [[float(request.form['R&D']), float(request.form['admin']),float(request.form["marketing"]),request.form["location"]]]
        data = [[float(request.form['R&D']), float(request.form['admin']),float(request.form["marketing"]),location]]
        # print(data)

        # onehotencoder = OneHotEncoder(categorical_features = [3])
        # print(onehotencoder)
        # data = onehotencoder.fit_transform(data).toarray()

        # Avoiding the Dummy Variable Trap
        # data = data[:, 1:]


        print("DAtA :      ")
        print(data)
        
        # print("Data", model.predict(data))
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict(data)
        print(prediction)

        # Take the first value of prediction
        output = prediction[0]

        return render_template("results.html", output=output, exp=data)

if __name__ == '__main__':
    app.run(debug=False)

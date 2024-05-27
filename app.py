#importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import random

#load the Random Forest Classifier model
file_name = 'models.pkl'
model = pickle.load(open(file_name,'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
        # Put all form entries values in a list 
    # features = [float(i) for i in request.form.values()]
    # Convert features to array
    # array_features = [np.array(features)]
    #predict features
    # prediction = model.predict(array_features)
    if request.method == 'POST':
        Id = random.randint(1,100)
        age = int(request.form.get('age'))
        sex = int(request.form['sex'][0])
        dataset = int(request.form['Dataset'][0])
        cp = int(request.form['cp'][0])
        trestbps = int(request.form.get('trestbps'))
        chol = int(request.form.get('chol'))
        fbs = int(request.form['fbs'][0])
        restecg = int(request.form['restecg'][0])
        thalch = int(request.form.get('age'))
        exang = int(request.form['exang'][0])
        oldpeak = int(request.form['oldpeak'][0])
        slope = int(request.form['slope'][0])
        ca = int(request.form['ca'][0])
        thal = int(request.form['thal'][0])

        data1 = np.array([[Id,age,sex,dataset,cp,trestbps,chol,fbs,restecg,thalch,exang,oldpeak,slope,ca,thal]])
        df = pd.DataFrame(data1, columns=['id','age','sex','dataset','cp','trestbps','chol','fbs','restecg','thalch','exang','oldpeak','slope','ca','thal'])
        print(df)
        prediction = model.predict(df)
        output = prediction

    if output==1:
            return render_template('result.html',result=f"The patient is likely to have a heart disease with severity {output}")
    else:
        return render_template('result.html',result="The patient is not likely to have a Heart disease")

     #Run the application   
if __name__ == '__main__':
    app.run(debug=True)
    print("Running")
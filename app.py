from flask import Flask,render_template,request
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
import pickle as pkl 
import numpy as np

scale = pkl.load(open('datafiles/scale.pkl','rb'))
model = pkl.load(open('datafiles/fuel_model.pkl','rb'))
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    distance = float(request.form['distance'])
    fuelPrice = round(model.predict(scale.transform(np.array(distance).reshape(-1,1)))[0],2)
    return render_template('predict.html',distance=distance,fuelPrice=fuelPrice)
if __name__ == '__main__':
    app.run(debug=True)
import requests
import numpy as np
from flask import Flask, request, jsonify,render_template
API_KEY = "tP0KjjEf6DX0Co2H4Ifbi88zwKPKVEQKQX-ga1GkbYYR"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def home1():
    return render_template('index.html')
@app.route('/predict')
def home2():
    return render_template('web.html')

@app.route('/login',methods = ['POST'])
def login():
    a=request.form['year1']
    b=request.form['year2']
    c=request.form['year3']
    d=request.form['year4']
    e=request.form['year5']
    f=request.form['year6']
    g=request.form['year7']
    h=request.form['year8']
    i=request.form['year9']
    j=request.form['year10']
    x_input = [a,b,c,d,e,f,g,h,i,j]
   
    for i in range(0, len(x_input)): 
        x_input[i] = float(x_input[i])
    
            
    x_input=np.array(x_input).reshape(1,-1)
    n_steps=10
    i=0
    while(i<1):
        x_input = x_input.reshape((n_steps,1))
        payload_scoring = {"input_data": [{"fields": [["Closing Value"]], "values": [x_input.tolist()]}]}
        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8c1f578c-e1b5-4d71-bec5-c60cc7f7b61c/predictions?version=2021-11-06', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
        yhat =response_scoring.json()
        i=i+1
        yhat=yhat['predictions'][0]['values'][0][0]
        return render_template('web.html',showcase = 'The next day predicted value is : '+str(yhat))
if __name__ =="__main__":
    app.run(debug = True)
    app.run(host = '0.0.0.0', port = 5000)

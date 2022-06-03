import requests
import numpy as np
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Mp56YZDyCufV9PZv7abM_Z-Cjyikajl4oWjnwf7jJK9e"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
a = 11
b = 22
c = 33
d = 44
e = 55
f = 66
g = 77
h = 88
i = 99
j = 84
k=int(j)
#print()
count=0
while(k!=0):
    k=k/10
    k=int(k)
    count = count+1
x_input = [a,b,c,d,e,f,g,h,i,j]
for i in range(0, len(x_input)): 
    x_input[i] = float(x_input[i])
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
x_input=scaler.fit_transform(np.array(x_input).reshape(-1,1))
#x_input=np.array(x_input).reshape(1,-1)


#print(x_input)
#for i in range(0,len(x_input)):
 #   print(x_input[i])
temp_input=list(x_input)
temp_input=temp_input[0].tolist()
lst_output=[]
n_steps=10
i=0
while(i<1):
    x_input = x_input.reshape((n_steps,1))
    
# NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": [["Closing value"]], "values": [x_input.tolist()]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8c1f578c-e1b5-4d71-bec5-c60cc7f7b61c/predictions?version=2021-11-06', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    predictions = response_scoring.json()
    print(predictions)
    #yhat = predictions['predictions'][0]['values'][0][0]
   # for i in range(0,count):
    #    yhat = yhat*10
    #print(yhat)
    #yhat = np.array(yhat)
   # yhat=yhat[0]
   # yhat=float(yhat)
   # for i in range(0,count):
    #    yhat=yhat*10
   # print(yhat)
   # i=i+1;
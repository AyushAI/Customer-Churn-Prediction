from flask import Flask, render_template, request
import pickle
import numpy as np



#To load the model back into your program
ml_model = "XGB_model.pkl"
with open(ml_model, 'rb') as file:
    loaded_model = pickle.load(file)


def label_encoding(list):
    list[2] = np.where(list[2]=='Male',1,0)
    list[1] = list[1].astype('category').cat.codes
    return list[0]

def Churn_prediction(result_data):
    result_data = label_encoding(result_data)
    prediction = np.array(list)
    result = loaded_model.predict(prediction)
    return result[0]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    result_data = request.form.to_list()
    print(result_data)
    result = Churn_prediction(result_data)
    if int(result) == 1:
        prediction = 'Sorry but the client is very likely to leave your Bank . . .'
    else:
        prediction = "Congrats ! the customer won't leave your Bank . . ."
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run()
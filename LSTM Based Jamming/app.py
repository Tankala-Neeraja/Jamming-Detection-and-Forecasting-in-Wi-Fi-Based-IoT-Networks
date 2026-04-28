#import python require classes and packages
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import os
#=================flask code starts here
from flask import Flask, render_template, request, redirect, url_for, session,send_from_directory
import pickle
from sklearn.metrics import accuracy_score
from keras.utils.np_utils import to_categorical
from keras.layers import Dense, Dropout, Activation, Flatten, LSTM, RepeatVector
from keras.models import Sequential, load_model, Model
from sklearn.metrics import accuracy_score
from keras.callbacks import ModelCheckpoint
from sklearn import svm
from keras.layers import  MaxPooling2D
from keras.layers import Convolution2D
import seaborn as sns
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.secret_key = 'welcome'

#loading normal wify dataset
df1 = pd.read_csv("Dataset/normal.csv")
df1['Class'] = 0
df1

#loading wifi jamming attack dataset
df2 = pd.read_csv("Dataset/jamming_gaussiannoise.csv")
df2['Class'] = 1
df2


#combining both datasets to form a single dataset with normal and jamming attack
dataset = pd.concat([df1, df2])
#apply dataset processing such as shuffling and normalization
data = dataset.values
X = data[:,0:data.shape[1]-1]
Y = data[:,data.shape[1]-1]
scaler = MinMaxScaler((0,1))
X = scaler.fit_transform(X)#normalize features
indices = np.arange(X.shape[0])
np.random.shuffle(indices)#shuffle features
X = X[indices]
Y = Y[indices]
print("Normalize Features = "+str(X))
#split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
print("Dataset Train & Test Split Details")
print("Number of records in Dataset : "+str(X.shape[0]))
print("Number of features found in Dataset : "+str(X.shape[1]))
print("80% records used to train algorithms : "+str(X_train.shape[0]))
print("20% records used to test algorithms : "+str(X_test.shape[0]))

#define global variables to save accuracy and other metrics
accuracy = []
precision = []
recall = []
fscore = []

@app.route('/Predict', methods=['GET', 'POST'])
def predictView():
    return render_template('Predict.html', msg='')

@app.route('/', methods=['GET', 'POST'])
def index():        
    return render_template('index.html', msg='')

@app.route('/index', methods=['GET', 'POST'])
def index1():
    return render_template('index.html', msg='')

@app.route('/AdminLogin', methods=['GET', 'POST'])
def AdminLogin():
    return render_template('AdminLogin.html', msg='')

@app.route('/AdminLoginAction', methods=['GET', 'POST'])
def AdminLoginAction():
    if request.method == 'POST' and 't1' in request.form and 't2' in request.form:
        user = request.form['t1']
        password = request.form['t2']
        if user == "admin" and password == "admin":
            return render_template('AdminScreen.html', msg="Welcome "+user)
        else:
            return render_template('AdminLogin.html', msg="Invalid login details")

@app.route('/Logout')
def Logout():
    return render_template('index.html', msg='')

def getModel():
    cnn2d_model = Sequential()
    cnn2d_model.add(Convolution2D(8, (1, 1), input_shape = (8, 1, 1), activation = 'relu'))
    cnn2d_model.add(MaxPooling2D(pool_size = (1, 1)))
    cnn2d_model.add(Convolution2D(4, (1, 1), activation = 'relu'))
    cnn2d_model.add(MaxPooling2D(pool_size = (1, 1)))
    cnn2d_model.add(Flatten())
    cnn2d_model.add(Dense(units = 16, activation = 'relu'))
    cnn2d_model.add(Dense(units = 2, activation = 'softmax'))
    cnn2d_model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    cnn2d_model.load_weights("model/cnn2d_weights.hdf5")
    return cnn2d_model

@app.route('/PredictAction', methods=['GET', 'POST'])
def PredictAction():
    if request.method == 'POST':
        labels = ['Normal', 'Jamming Attack']
        test_data = pd.read_csv("Dataset/testData.csv")#read test data values
        temp = test_data.values
        test_data = scaler.transform(temp)#normalize test data
        test_data = np.reshape(test_data, (test_data.shape[0], test_data.shape[1], 1, 1))#convert data to CNN2D 2 dimension format
        cnn_2d_model = getModel()
        predict = cnn_2d_model.predict(test_data)#perform prediction on test data
        output = ""
        for i in range(len(predict)):
            y_pred = np.argmax(predict[i])
            output += "Test Data = "+str(temp[i])+" Predicted Output ====> "+labels[y_pred]+"<br/><br/>"
        return render_template('AdminScreen.html', msg=output)

if __name__ == '__main__':
    app.run()


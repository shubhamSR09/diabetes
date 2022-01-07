from flask import Flask, render_template,request
import pickle
import numpy as np

//filename = 'new_diabetes.pkl'
//lr = pickle.load(open(filename, 'rb'))


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('templates/demo1.html')
    

if __name__ == '__main__':
    app.run(debug=True)

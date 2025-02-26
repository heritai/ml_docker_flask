#pip install flask
from flask import Flask, jsonify, request

import paq as q



# start flask
app = Flask(__name__)


# render default webpage
@app.route('/')
def home():
    message="API is set up"
    return jsonify(message)

@app.route('/functions')
def func():
    return q.__all__


def calc_wrap(problem, n_samples, n_features):
    try:
        X, y = q.generate(problem, n_samples, n_features)
        stats = q.statistics(X, y)
        model, error = q.learn(problem, X, y)
        predictions = q.predict(model, problem)
        return stats, error, predictions
    except Exception as e:
        err_txt= str(e)
        return jsonify(err_txt +" : problem type is not specified! \n for the classfication problems go to /classification/process and for the regression problems go to /regression/process")
    

@app.route('/process', methods = ['POST'])
def process():
    if request.method == 'POST':
        inputt = request.form.to_dict()
        n_samples = int(inputt['n_samples'])
        n_features= int(inputt['n_features'])
        problem="none"
        return calc_wrap(problem, n_samples, n_features)


@app.route('/classification/process', methods = ['POST'])
def classification_process():
    if request.method == 'POST':
        inputt = request.form.to_dict()
        n_samples = int(inputt['n_samples'])
        n_features= int(inputt['n_features'])
        problem="classification"
        stats, error, predictions = calc_wrap(problem, n_samples, n_features)
        return jsonify({'stats':str(stats), 'error':str(error), 'predictions':str(predictions)})



@app.route('/regression/process', methods = ['POST'])
def regression_process():
    if request.method == 'POST':
        inputt = request.form.to_dict()
        n_samples = int(inputt['n_samples'])
        n_features= int(inputt['n_features'])
        problem="regression"
        stats, error, predictions =calc_wrap(problem, n_samples, n_features)
        return jsonify({'stats':str(stats), 'error':str(error), 'predictions':str(predictions)})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# important to set these arguments whith docker
# host='0.0.0.0', port=5000

#FLASK_APP=flsk.py flask run
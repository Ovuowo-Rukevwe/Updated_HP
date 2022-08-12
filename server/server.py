from flask import Flask, request, jsonify, app
from flask_cors import CORS, cross_origin

import util


def create_app():
    app = Flask(__name__)
    CORS(app)


@app.route('/get_location_names')
@cross_origin()
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
@cross_origin()
def predict_home_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, sqft, bhk, bath)
    })

    response.headers.add('Access-control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print('starting a python project')
    util.load_saved_artifacts()
    app.run()

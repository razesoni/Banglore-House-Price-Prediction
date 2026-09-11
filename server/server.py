import os

from flask import Flask, jsonify, request, send_from_directory
import util

CLIENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'client'))
app = Flask(__name__, static_folder=CLIENT_DIR, static_url_path='')

@app.route('/')
def index():
    return send_from_directory(CLIENT_DIR, 'app.html')

@app.route('/api/get_location_names')
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/predict_home_price', methods=['POST'])
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    location = request.form['location']
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
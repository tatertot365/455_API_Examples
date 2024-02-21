from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/charges_api', methods=['POST'])
def charges_api():
    data = request.get_json()
    age = int(data['age'])
    bmi = int(data['bmi'])
    children = int(data['children'])
    
    with open('sample_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    prediction = model.predict([[age, bmi, children]])

    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
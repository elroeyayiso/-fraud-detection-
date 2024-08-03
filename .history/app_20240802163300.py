from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    feature1 = data.get('feature1')
    # Dummy prediction logic for illustration
    prediction = 1 if feature1 == 'suspicious_value' else 0
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)

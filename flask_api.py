from flask import Flask, request, jsonify
import pandas as pd
import joblib
from scripts import prepare_request as prep

app = Flask(__name__)

model = joblib.load('optimised_model.pkl')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        df = pd.DataFrame(data)
        
        X_test = prep.prepare_data_request(df)  
        # return jsonify({'error': str(X_test)})

        prediction = model.predict(X_test)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=25565)

from flask import Flask, request, jsonify
import numpy as np
import joblib  # Assuming you saved your model using joblib
import librosa  # For audio processing\
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), 'model.sav')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        age = float(request.form['age'])
        sex = 1 if request.form['sex'].lower() == 'male' else 0
        audio_file = request.files['audio']

        # Process audio file
        y, sr = librosa.load(audio_file, sr=None)
        mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=3).T, axis=0)  # Adjust n_mfcc to 3

        # Prepare input data for the model
        input_data = np.array([age, sex] + mfccs.tolist()).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data)

        # Return the result
        result = 'yes' if prediction[0] == 1 else 'no'
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

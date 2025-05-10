from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from audio_features import extract_audio_features

app = Flask(__name__)

# # Load your saved model
# with open("best_random_forest_model.pkl", "rb") as f:
#     model = pickle.load(f)

# print("Model Loaded Successfully !!")

# # Route for the main page
# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/services')
# def services():
#     return render_template("services.html")

# @app.route('/future')
# def future():
#     return render_template("future.html")

# @app.route('/about')
# def about():
#     return render_template("AboutUs.html")

# @app.route('/parkinsons')
# def parkinsons():
#     return render_template("parkinsons.html")

# @app.route('/diabetes')
# def diabetes():
#     return render_template("diabetes.html")

# @app.route('/heart')
# def heart():
#     return render_template("heart.html")

# # Endpoint for predictions
# @app.route('/predict', methods=['POST'])
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Check if an audio file is provided
#     if 'voice-sample' in request.files:
#         audio_file = request.files['voice-sample']
        
#         try:
#             # Extract features from the audio file
#             features = extract_audio_features(audio_file)  # Pass the file object directly
            
#             features_array = np.array([[features['jitter'], features['shimmer'], features['nhr']]])
            
#             # Predict with the model
#             prediction = model.predict(features_array)
#             result_message = "High Risk of Parkinson's" if prediction[0] == 1 else "Low Risk of Parkinson's"
            
#             return jsonify({"result": result_message})

#         except Exception as e:
#             return jsonify({"error": str(e)}), 500  # Return the error message

#     # If no audio, check for manual feature input
#     jitter = request.form.get('jitter', type=float)
#     shimmer = request.form.get('shimmer', type=float)
#     nhr = request.form.get('nhr', type=float)
#     if jitter is not None and shimmer is not None and nhr is not None:
#         features_array = np.array([[jitter, shimmer, nhr]])
#         prediction = model.predict(features_array)
#         result_message = "High Risk of Parkinson's" if prediction[0] == 1 else "Low Risk of Parkinson's"
        
#         return jsonify({"result": result_message})

#     return jsonify({"error": "No valid audio or feature data provided."}), 400


# Load the heart disease prediction model
with open("heart_model.pkl", "rb") as f:
    heart_model = pickle.load(f)

print("Heart Disease Model Loaded Successfully!")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/future')
def future():
    return render_template("future.html")

@app.route('/about')
def about():
    return render_template("AboutUs.html")

@app.route('/parkinsons')
def parkinsons():
    return render_template("parkinsons.html")

@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")

@app.route('/heart')
def heart():
    return render_template("heart.html")

# Endpoint for heart disease prediction
@app.route('/predict_heart', methods=['POST'])
def predict_heart():
    try:
        # Collect data from the form
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        # Create feature array for prediction
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Predict using the heart model
        prediction = heart_model.predict(features)
        result_message = "High Risk of Heart Disease" if prediction[0] == 1 else "Low Risk of Heart Disease"

        return jsonify({"result": result_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

# # Test route
# @app.route('/test')
# def test():
#     return "Flask is running!"

# if __name__ == '__main__':
#     app.run(debug=True)
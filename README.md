# 🩺 Health & Parkinson's Disease Prediction Web App

This project is a machine learning powered web application built using **Flask** to detect two major health conditions:

- **Heart Disease** (based on structured medical data)
- **Parkinson's Disease** (based on audio signal features)

It uses trained models, audio processing, and clean web UI to allow users to test predictions in real time.

---

## 🚀 Features

- 💓 Predict **Heart Disease** using clinical parameters.
- 🧠 Detect **Parkinson’s Disease** from a user's voice.
- 🔊 Audio feature extraction using `librosa` for Parkinson’s.
- 🌐 Flask-based web application with templates and static files.
- 📁 Organized folder structure for easy extension and deployment.

---

## 🗂️ Project Structure

```text
.
├── app.py                         # Flask backend
├── audio_features.py             # Voice feature extractor for Parkinson's
├── uploaded_audio.wav            # Sample audio file
├── templates/                    # HTML templates
├── static/                       # CSS, images, etc.
├── requirements.txt              # Python dependencies
├── Heart_Disease.ipynb           # Heart disease model training notebook
├── Parkinssons_new.ipynb         # Parkinson's model training notebook
├── Parkinssons_new_1.ipynb       # Alternate/experimental notebook
├── best_model.pkl                # A trained model (likely Parkinson's)
├── heart_model.pkl               # Final model for heart disease
├── heart-disease.csv             # Heart dataset
├── parkinsons/
│   ├── Parkinsson_disease.csv    # Parkinson’s dataset
│   ├── best_model.joblib         # Best Parkinson’s model
│   ├── best_random_forest_model.pkl  # Random Forest model
│   ├── grid_search_results.joblib   # Grid search results
```

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### 2. Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Run the Application
python app.py
Visit http://127.0.0.1:5000 in your browser.

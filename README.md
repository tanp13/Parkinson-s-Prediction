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
├── app.py                        # Flask application
├── audio_features.py            # Extracts features from voice
├── uploaded_audio.wav           # Sample voice file
├── templates/                   # HTML templates for frontend
├── static/                      # Static files (CSS/images)
├── requirements.txt             # Python dependencies
├── Heart_Disease.ipynb          # Heart disease model training
├── Parkinssons_new.ipynb        # Parkinson’s disease model training
├── best_model.pkl               # Trained model (possibly Parkinson’s)
├── heart_model.pkl              # Final heart model
├── heart-disease.csv            # Heart dataset
├── parkinsons/
│   ├── Parkinsson_disease.csv   # Parkinson’s dataset
│   ├── best_model.joblib        # Best model for Parkinson’s
│   ├── best_random…model.pkl  # Random forest Parkinson’s model
│   ├── grid_search_results.joblib # Grid search results

---

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

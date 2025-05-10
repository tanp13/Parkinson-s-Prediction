import numpy as np
import librosa
import parselmouth
from parselmouth.praat import call
import tempfile

def extract_audio_features(audio_file):
    """
    Extracts jitter, shimmer, and noise-to-harmonic ratio (NHR) from an audio file.
    
    Parameters:
    - audio_file: The audio file object (e.g., from a file upload or recorded data).

    Returns:
    - Dictionary with jitter, shimmer, and NHR values.
    """
    # Save the audio data temporarily
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
        audio_file.save(temp_audio_file.name)  # Save the file directly from the FileStorage object
        temp_audio_path = temp_audio_file.name

        # Load the audio file for feature extraction
        y, sr = librosa.load(temp_audio_path, sr=None)
        
        # Convert to Parselmouth Sound object for Praat features
        snd = parselmouth.Sound(temp_audio_path)
        
        # Jitter (pitch variation)
        jitter = call(snd, "Get jitter (local)", 0.0, 0.02, 1.3)
        
        # Shimmer (amplitude variation)
        shimmer = call(snd, "Get shimmer (local)", 0.0, 0.02, 1.3)
        
        # Noise-to-Harmonics Ratio (NHR) calculation
        harmonicity = call(snd, "Get harmonics-to-noise ratio", 0.0, 0.02)
        nhr = 1 / harmonicity if harmonicity != 0 else 0  # Avoid division by zero

    # Return the features in a dictionary format for prediction
    return {
        "jitter": jitter,
        "shimmer": shimmer,
        "nhr": nhr
    }
import cv2
import numpy as np
from deepface import DeepFace

def get_emotion(img):
    try:
        result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        return result['dominant_emotion']
    except:
        return None

def extract_features(img):

    emotion = get_emotion(img)

    if emotion is None:
        return None

    # Fake the other features (simple heuristics or defaults)
    features = {
        "emotion": emotion,
        "skin": "oily",
        "eye_state": "sleepy",
        "face_shape": "other",
        "hairline": "normal",
        "ethnicity": "south_asian",
        "pose": "close"
    }

    return features

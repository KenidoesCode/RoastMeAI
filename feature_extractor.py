import cv2
import numpy as np
from fer import FER

# FER emotion detector
detector = FER()

def get_emotion(img):
    try:
        res = detector.detect_emotions(img)
        if not res:
            return None
        emotions = res[0]["emotions"]
        return max(emotions, key=emotions.get)
    except:
        return None

def extract_features(img):
    emotion = get_emotion(img)

    if emotion is None:
        return None

    # Simple static features for roasting engine
    return {
        "emotion": emotion,
        "skin": "oily",
        "eye_state": "sleepy",
        "face_shape": "other",
        "hairline": "normal",
        "ethnicity": "south_asian",
        "pose": "close"
    }

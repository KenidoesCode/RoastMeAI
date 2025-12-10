import cv2
import numpy as np
from fer import FER

detector = FER()

def get_emotion(img):
    res = detector.detect_emotions(img)
    if not res:
        return None
    return max(res[0]['emotions'], key=res[0]['emotions'].get)

def extract_features(img):
    """ Fake all non-emotion features (safe for cloud). """

    emotion = get_emotion(img)

    # fallback if no detection
    if emotion is None:
        return None

    return {
        "emotion": emotion,
        "skin": "oily",       # placeholder
        "eye_state": "sleepy",
        "face_shape": "round",
        "hairline": "normal",
        "ethnicity": "south_asian",
        "pose": "close"
    }

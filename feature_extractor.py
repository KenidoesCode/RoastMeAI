import numpy as np

def get_emotion(img):
    # Mock emotion detection for deployment
    emotions = ["happy", "sad", "angry", "surprised", "neutral"]
    return np.random.choice(emotions)

def extract_features(img):
    emotion = get_emotion(img)

    if emotion is None:
        return None

    return {
        "emotion": emotion,
        "skin": "oily",
        "eye_state": "sleepy",
        "face_shape": "other",
        "hairline": "normal",
        "ethnicity": "south_asian",
        "pose": "close"
    }

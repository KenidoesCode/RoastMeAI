import cv2
import numpy as np
from fer import FER
import mediapipe as mp

detector = FER()
mp_face_mesh = mp.solutions.face_mesh

def get_emotion(img):
    res = detector.detect_emotions(img)
    if not res:
        return None
    return max(res[0]['emotions'], key=res[0]['emotions'].get)

def get_face_landmarks(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img.shape
    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1) as mesh:
        r = mesh.process(img_rgb)
        if not r.multi_face_landmarks:
            return None
        pts = []
        for lm in r.multi_face_landmarks[0].landmark:
            pts.append((int(lm.x*w), int(lm.y*h)))
        return pts

def estimate_face_shape(landmarks):
    if len(landmarks) < 468:
        return "unknown"
    jaw_width = abs(landmarks[234][0] - landmarks[454][0])
    face_height = abs(landmarks[10][1] - landmarks[152][1])

    if jaw_width > face_height * 0.8:
        return "round"
    elif face_height > jaw_width * 1.2:
        return "long"
    return "other"

def estimate_hairline(landmarks):
    fh = landmarks[10][1] - landmarks[109][1]
    if fh > 70:
        return "receding"
    return "normal"

def detect_pose(landmarks):
    nose = landmarks[1]
    chin = landmarks[152]

    if nose[0] < chin[0] - 20:
        return "tilted"
    if abs(nose[1] - chin[1]) < 20:
        return "side"
    return "close"

def estimate_skin(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    brightness = hsv[...,2].mean()
    if brightness < 60:
        return "dry"
    if brightness > 160:
        return "oily"
    return "acne"

def extract_features(img):
    landmarks = get_face_landmarks(img)
    if landmarks is None:
        return None

    return {
        "emotion": get_emotion(img),
        "skin": estimate_skin(img),
        "eye_state": "sleepy",
        "face_shape": estimate_face_shape(landmarks),
        "hairline": estimate_hairline(landmarks),
        "ethnicity": "south_asian",
        "pose": detect_pose(landmarks)
    }

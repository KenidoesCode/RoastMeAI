import streamlit as st
import cv2
import numpy as np
from PIL import Image

from feature_extractor import extract_features
from roast_engine import inferno_roast

st.title("🔥 INFERNO MODE — LIVE RoastMe.AI 🔥")

mode = st.radio("Choose Mode:", ["Upload Image", "Live Camera Roast"])

if mode == "Upload Image":
    file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if file:
        img = Image.open(file)
        img_np = np.array(img)

        st.image(img_np, caption="Your Image", width=400)

        feats = extract_features(cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR))
        if feats:
            roast = inferno_roast(feats)
            st.error(roast)
        else:
            st.warning("Couldn’t detect a face.")

else:
    camera = st.camera_input("Turn on your camera for LIVE roast")

    if camera:
        img = Image.open(camera)
        img_np = np.array(img)

        st.image(img_np, caption="LIVE Frame", width=400)

        feats = extract_features(cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR))
        if feats:
            roast = inferno_roast(feats)
            st.error(roast)
        else:
            st.warning("Face not detected.")

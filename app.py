import streamlit as st
import cv2
import numpy as np
from PIL import Image

from feature_extractor import extract_features
from roast_engine import inferno_roast

# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------
st.set_page_config(page_title="RoastMe.AI", page_icon="🔥")

# ---------------------------------------------------------
# WARNING POPUP
# ---------------------------------------------------------
warning_html = """
<script>
    setTimeout(function() {
        alert("⚠️ WARNING: This will hurt your feelings. 
Proceed only if you're emotionally stable.");
    }, 800);
</script>
"""
st.markdown(warning_html, unsafe_allow_html=True)

# ---------------------------------------------------------
# LOGO + TITLE
# ---------------------------------------------------------
st.markdown(
    "<h1 style='text-align:center; color:#ff2e2e;'>🔥 RoastMe.AI By Pranauv 🔥</h1>",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# MODE SELECTOR
# ---------------------------------------------------------
mode = st.radio("Choose Mode:", ["Upload Image", "Live Camera Roast"])

# ---------------------------------------------------------
# UPLOAD MODE
# ---------------------------------------------------------
if mode == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        img_np = np.array(img)

        st.image(img_np, caption="Your Image", width=400)

        features = extract_features(cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR))

        if features:
            roast = inferno_roast(features)
            st.error(roast)
        else:
            st.warning("⚠️ No face detected. Try another image.")

# ---------------------------------------------------------
# LIVE CAMERA MODE
# ---------------------------------------------------------
else:
    camera_capture = st.camera_input("Turn on your camera for a LIVE roast")

    if camera_capture:
        img = Image.open(camera_capture)
        img_np = np.array(img)

        st.image(img_np, caption="LIVE Frame", width=400)

        features = extract_features(cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR))

        if features:
            roast = inferno_roast(features)
            st.error(roast)
        else:
            st.warning("⚠️ Couldn't detect your face bro...")

# ---------------------------------------------------------
# UI THEME (CSS)
# ---------------------------------------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0d0d0d;
}

h1 {
    font-weight: 900 !important;
}

.stButton>button {
    background-color: #ff2e2e;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #cc0000;
}

img {
    border-radius: 10px;
}

[data-testid="stFileUploader"] {
    color: white;
}
</style>
""", unsafe_allow_html=True)

import streamlit as st
import numpy as np
from PIL import Image

from feature_extractor import extract_features
from roast_engine import inferno_roast

st.set_page_config(page_title="RoastMe.AI", page_icon="🔥")

warning_html = """
<script>
    setTimeout(function() {
        alert("⚠️ WARNING: This will hurt your feelings.\nProceed only if you're emotionally stable.");
    }, 800);
</script>
"""
st.markdown(warning_html, unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align:center; color:#ff2e2e;'>🔥 RoastMe.AI By Pranauv 🔥</h1>",
    unsafe_allow_html=True
)

mode = st.radio("Choose Mode:", ["Upload Image", "Live Camera Roast"])

# -------------------------
# UPLOAD IMAGE
# -------------------------
if mode == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        img_np = np.array(img)

        st.image(img_np, width=400)

        features = extract_features(img_np)

        if features:
            st.error(inferno_roast(features))
        else:
            st.warning("No face detected.")

# -------------------------
# LIVE CAMERA
# -------------------------
else:
    camera_capture = st.camera_input("Turn on your camera")

    if camera_capture:
        img = Image.open(camera_capture)
        img_np = np.array(img)

        st.image(img_np, width=400)

        features = extract_features(img_np)

        if features:
            st.error(inferno_roast(features))
        else:
            st.warning("Face not detected.")

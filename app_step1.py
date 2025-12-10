# app_step1.py
import streamlit as st            # Streamlit builds the webpage
from PIL import Image             # Pillow handles images
import numpy as np                # numpy handles arrays (images as numbers)

st.set_page_config(page_title="RoastMe — Friendly Demon", page_icon="😈")

st.title("RoastMe.AI — Turn on camera or upload a picture 👇")

# two ways to give a photo: camera or upload
cam_img = st.camera_input("Turn on your camera (or skip)")
upload = st.file_uploader("Or upload an image", type=["jpg", "jpeg", "png"])

# prefer camera if given, else uploaded file
image = None
if cam_img:
    image = Image.open(cam_img)
elif upload:
    image = Image.open(upload)

if image:
    st.subheader("Nice! Here's your image:")
    st.image(image, use_column_width=True)
    # convert to numpy array so later code can use it easily
    img_arr = np.array(image)
    st.write("Image shape:", img_arr.shape)
else:
    st.info("No image yet — use camera or upload a photo to get roasted 😈")

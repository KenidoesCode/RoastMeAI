import streamlit as st

st.set_page_config(page_title="RoastMe.AI", page_icon="🔥")

st.markdown("""
<div style="text-align:center; margin-top:50px;">
    <h1 style="color:#ff2e2e;">🔥 RoastMe.AI 🔥</h1>
    <h3 style="color:white;">The world's first DEMON MODE roasting AI</h3>
    <p style="color:gray;">Turn on your camera or upload a picture to receive the most disrespectful roast of your entire existence.</p>

    <p style="margin-top:20px; color:#ff2e2e;">
        ⚠️ Warning: Emotional damage guaranteed.
    </p>

    <a href="app" style="
        background:#ff2e2e;
        padding:12px 25px;
        border-radius:10px;
        color:white;
        text-decoration:none;
        font-size:20px;
        font-weight:bold;">
        Enter RoastMe.AI →
    </a>
</div>
""", unsafe_allow_html=True)

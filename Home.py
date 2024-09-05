import streamlit as st
from datetime import datetime
import requests
from streamlit_lottie import st_lottie
import json

st.set_page_config(
    page_title="Apllication System",
    page_icon=":brain:",
    layout="wide"
)

st.title("Home")
st.divider()

# def load_lottiefile(filepath: str):
#     with open(filepath, "r") as f:
#         return json.load(f)

# lottie_animation = load_lottiefile("img/animation.json")

# Display animation
# if lottie_animation:
#     st_lottie(lottie_animation, height=300, key="mental_health")

st.write("# Welcome to the Mental Health Identification System")
st.write(
    """
    Aplikasi ini hanya untuk identifikasi dini terkait kesehatan mental dan bukan sebagai acuan diagnosis medis. Misi kami adalah menyediakan platform yang andal dan mudah digunakan untuk mengidentifikasi masalah kesehatan mental di kalangan Generasi Z. Dengan algoritma pohon keputusan yang canggih, kami berupaya memberikan hasil yang akurat serta sumber daya yang bermanfaat bagi pengguna. Namun, kami menyarankan untuk berkonsultasi dengan profesional kesehatan mental untuk diagnosis dan perawatan lebih lanjut.
    """
)

st.write("### Let's Get Started!")

# Footer
st.write("---")
st.write("© 2024 Identification Of Mental Health App. All rights reserved.")

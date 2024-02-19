import streamlit as st
from pathlib import Path

css_file = "styles/Education.css"
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)



# --- WORK HISTORY ---
st.write("---")
st.subheader("Thesis")
st.write("---")

st.write("📖", " Ph.D. student | University of Montpellier, (France) - USMBA of Fez, (Morocco)")
st.write("03/2020 - 09/2023")
st.write(
    """
Thesis topic: Deep Learning approach for ultrasonic signal processing.
- Propose a method for time-of-flight estimation on ultrasonic signals that outperforms existing methods on 99% of samples.
- Provide an Attention Unet for noise reduction on ultrasonic signals allowing for a 30 dB enhancement in SNR.
- Leverage the proposed Attention Unet for the deconvolution of overlapping echoes and conduct an improvement of the axial resolution of the final ultra- sound images.
- Implementation of these techniques in an acoustic microscope.
- Validation on Sicilium samples, allowing for precise thickness measurement and the detection of flatness defects.
"""
)


# --- WORK HISTORY ---
st.write("---")
st.subheader("Education")
st.write("---")

st.write("📖", "Engineer’s degree in Mechanical and automated systems engineering | ENSA - Fez")
st.write("09/2013 - 07/2019")
st.write(
    """
"""
)
st.write('\n')
st.write("📖", "Higher School Diploma | College Mly Slimane - Fez")
st.write("2013")





import base64
import streamlit as st
from pathlib import Path
from PIL import Image
import webbrowser


css_file = "styles/Projects.css"
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

zellig = Image.open('assets/robot zellig.png')




# --- Projects & Accomplishments ---
st.write("---")
st.subheader("Projects")
st.write("---")

st.write(f'<div style="font-size: 15pt; font-weight: 800;"> Heart rate measurement using ECG data for epilipsy prediction</div>', unsafe_allow_html=True)
st.write('Paddling and breaking forecasting for improved assistance of surfers.')
if st.button('Show more', key="jednzzke"):
    st.write(' - Deconvolution of QRSs for R-peaks detection using Attention Unet')
    st.write(' - HR deriving and variability detection')
    st.write(' - ')

st.divider()

st.write(f'<div style="font-size: 15pt; font-weight: 800;"> Stand-up assisted surfing</div>', unsafe_allow_html=True)
st.write('Paddling and breaking forecasting for improved assistance of surfers.')
if st.button('Show more', key="jednzzke1"):
    st.write(' - Deconvolution of QRSs for R-peaks detection using Attention Unet')
    st.write(' - HR deriving and variability detection')
    st.write(' - ')

st.divider()

st.write(f'<div style="font-size: 15pt; font-weight: 800;"> SOLAR DECATHLON Africa</div>', unsafe_allow_html=True)
st.write('Design and build an autonomous house running solely on solar power.')

url = 'https://www.solardecathlonafrica.com/fr/team-golden-ryad/'
if st.button('Visit website'):
    webbrowser.open_new_tab(url)



st.divider()

st.write(f'<div style="font-size: 15pt; font-weight: 800;"> Traditional mosaic of Fez</div>', unsafe_allow_html=True)
st.write('Smart positioning of mosaic using computer vision techniques and a robotic arm.')
if st.button('Show more', key="jednze"):
    st.image(zellig)
    st.write(' - Classification of mosaics according to shape and color')
    st.write(' - Place the mosaics using a robotic arm controlled by an Arduino card')

st.divider()


st.write(f'<div style="font-size: 15pt; font-weight: 800;"> Smart surveillance robot</div>', unsafe_allow_html=True)
st.write('Design and construction of a remote-controlled surveillance robot.')
if st.button('Show more',key="jedn"):
    st.write(' - Motion detection surveillance robot implemented on a Raspberry Pi card')
    st.write(' - L298N card use for motors control')
    st.write(' - Raspberry Pi module camera use for supervision')












import streamlit as st
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = 'styles/Certifications.css'

cerfits = [{'Title':'Neural Networks and Deep Learning', 
            'Univ':'Coursera'},

            {'Title':'Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization', 
            'Univ':'Coursera'},

            {'Title':'Structuring Machine Learning Projects', 
            'Univ':'Coursera',
            'Link': 'https://coursera.org/verify/DXTFR3XBLYAN'},

            {'Title':'Convolutional Neural Networks', 
            'Univ':'Coursera',
            'Link': 'https://coursera.org/verify/Q3RLJ7ZWEZFS'},

            {'Title':'Sequence Models', 
            'Univ':'Coursera',
            'Link': 'https://coursera.org/verify/A7EVHHEFFYL9'}, 
            
            {'Title':'Custom Models, Layers, and Loss Functions with TensorFlow', 
            'Univ':'Coursera',
            'Link': 'https://coursera.org/verify/NLWYE8FS87BH'}, 
        ]


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- Technical certifications ---
st.write("---")
st.subheader("Technical certifications")
st.write("---")
for c in cerfits:
    st.write(f'<div style="font-size: 15pt; font-weight: 800;"> {c.get("Title")}</div>', unsafe_allow_html=True)
    st.write(f'<div style="font-size: 15pt; font-weight: 400;"> {c.get("Univ")}</div>', unsafe_allow_html=True)
    if c.get('Link'):
        st.write(f"[Link]({c.get('Link')})")
    st.divider()

# --- Academic certifications ---
cerfits_A = [
            {'Title':'Scientific integrity in the research professions', 
            'Univ':'University of Bordeaux'},
            {'Title':'Teaching at university: teaching methods and digital tools', 
            'Univ':'University of Montpellier',}]



st.subheader("Academic certifications")
st.write("---")
for c in cerfits_A:
    st.write(f'<div style="font-size: 15pt; font-weight: 800;"> {c.get("Title")}</div>', unsafe_allow_html=True)
    st.write(f'<div style="font-size: 15pt; font-weight: 400;"> {c.get("Univ")}</div>', unsafe_allow_html=True)
    st.divider()
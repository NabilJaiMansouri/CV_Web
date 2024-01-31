from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "Home.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Profil.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Nabil JAI MANSOURI"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
#with open(resume_file, "rb") as pdf_file:
#    PDFbyte = pdf_file.read()


#----------------------------------------------
# Intro
#----------------------------------------------
profile_pic = Image.open(profile_pic, )
NAME = "Nabil JAI MANSOURI"
DESCRIPTION = """ Ph.D. in Deep Learning and Ultrasound Imaging, enthralled by the advancements in Machine Learning, 
with a focus on enhancing the capabilities of ultrasound imaging techniques by leveraging and refining Deep Learning 
methods. You are welcome to look at my Google Scholar profile for a deeper understanding of my Research field.\n 

With an overwhelming passion for research and innovation, I’m open to any collaborative research work. Being 
adventurous, I appreciate new challenges that necessitate exploring and discovering new things.
"""
col1, col2 = st.columns([0.45, 0.65], gap="medium")
with col1:
    st.image(profile_pic)

with col2:
    st.markdown(f'<h1 style="text-align: center;">{NAME}</h1>',unsafe_allow_html=True)
    st.divider()
    st.write(f'<div style="text-align: justify;">{DESCRIPTION}</div>', unsafe_allow_html=True)

#----------------------------------------------
# Contacts
#----------------------------------------------
EMAIL = "nabiljaimansouri@gmail.com"
Phones = ["+33 6 52 14 55 86", "+212 6 73 60 43 09"]

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/nabil-jai-mansouri-ph-d-43b92b154/",
    "Google scholar": "https://scholar.google.com/citations?user=PmxP7FoAAAAJ&hl=fr&oi=ao",
    "Scopus": "https://www.scopus.com/authid/detail.uri?authorId=58038118900",
    
}

st.divider()
cols = st.columns([0.4, 0.3, 0.3], gap="medium")
with cols[0]:
    st.write(f'<div style="text-align: center;"> 📧 {EMAIL}</div>', unsafe_allow_html=True)


for i in range(len(Phones)):
    with cols[i+1]:
        st.write(f'<div style="text-align: center;"> 📞 {Phones[i]}</div>', unsafe_allow_html=True)

st.divider()
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")






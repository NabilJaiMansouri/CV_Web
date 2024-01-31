import streamlit as st
from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#----------------------------------
# Create some sample text
text = ' Deep Learning, Machine Learning, Ultrasound imaging, Acoustic microscopy, Image processing, Signal processing, Data science, Computer vision, NLP, Speech processing, AWS, GCP'
# Create and generate a word cloud image:
wordcloud = WordCloud(background_color="rgba(255, 255, 255, 0)", mode="RGBA").generate(text)
# Display the generated image:
fig, ax = plt.subplots()
ax.imshow(wordcloud)
ax.axis("off")
fig.set_facecolor((1.0, 1.0, 1.0, 0))
st.pyplot(fig)
#----------------------------------


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = 'styles/Skills.css'

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- SKILLS ---
st.write('\n')
st.header("Skills")
st.write("---")
st.write(
    """ 
  <div style="font-size: 15pt; font-weight: 800;"> 🔭 Technical</div> \n
 Deep Learning, Machine Learning, Ultrasound imaging, Acoustic microscopy, Image and signal processing,  Data science, Computer vision, Natural language processing\n
 <div style="font-size: 15pt; font-weight: 800;"> 👩‍💻 Programming</div>\n
Python, OOP, Matlab, Labview, C++, html, CSS, Javascript \n
 <div style="font-size: 15pt; font-weight: 800;"> 📊 Data Visualisation</div> \n
 Matplotlib, MS Excel, Plotly, Seaborn \n
  <div style="font-size: 15pt; font-weight: 800;"> 📚 MLOps/DevOps</div> \n
 MLflow, ClearML, WandB, Git, CI/CD, Docker, Rest API, ...\n
  <div style="font-size: 15pt; font-weight: 800;"> 🗄️ Databases</div> \n
 MongoDB, MySQL \n
"""
, unsafe_allow_html=True)

# --- Languages ---
st.write('\n')
st.header("Languages")
st.write("---")


col1, col2 = st.columns(2)
col1.header("🇫🇷  French")
col1.write("C1")


col2.header("🇺🇸  English")
col2.write("C1")


col3, col4 = st.columns(2)
col3.header("🇩🇪  German")
col3.write("A2")

col4.header("🇲🇦  Arabic")
col4.write("C2")



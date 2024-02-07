import streamlit as st
from pathlib import Path

css_file = "styles/Work.css"
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- WORK HISTORY ---
st.write("---")
st.subheader("Professional experiences")
st.write("---")

# --- JOB 1
st.write("💼", "**Data scientist | IES - Montpellier**")
st.write("11/2023 - 01/2024")
st.write(
    """
- Tuna’s vocalization detection on underwater sound recordings. \n
- Features engineering and unsupervised learning for signals clustering. \n
- Analyzing species behavior in order to preserve biodiversity.\n
"""
)
st.write("\n")


# --- JOB 2
st.write("💼", "**ML Engineer | ÖSD - Fez**")
st.write("01/2023 - 07/2023")
st.write(
    """
- Software development (web/desktop app) for automatic grading of MCQ. 
- Build annotated data sets of hand-written answers from MCQ.
- Establish a Deep Learning model whose performance is monitored and improved in order to maintain its accuracy above 99%.
- Analyze the candidates’ grades and communicate reports. 
- Reduced the task’s processing time by 95%."""
)
st.write("\n")

st.write(
    """
- Auto form filling and webpage scrapping for information collection.
- Reduced the task’s processing time by 98%."""
)
st.write("\n")

st.write(
    """
- OCR model deployment for reading candidates' names on IDs and final degrees.
- Reduce the error risk to less than 1%.
"""
)

st.write("---")
st.subheader("Academic experiences")
st.write("---")

# --- JOB 3
st.write("💼", "**Teacher | National School of Applied Sciences - Fez**")
st.write("09/2022 - 12/2022")
st.write(
    """
- Higher education - Introduction to C++ programming language.
"""
)

st.write("---")
st.subheader("Internships")
st.write("---")

# --- JOB 4
st.write("💼", "**Intern | IES - Montpellier**")
st.write("04/2019 - 07/2019")
st.write(
    """
- Build a dataset of ultrasound images and their corresponding optic version. 
- Build a RNN forecasting model and an Auto-regressive model for missing data imputation on Ultrasound images of granular structure materials.
- Analyze the weak points of each method.
- Develop a UI to tweak the methods’ parameters and operate the missing data imputation.
"""
)
st.write("\n")


# --- JOB 5
st.write('\n')
st.write("💼", "**Intern | LAFARGE HOLCIM - Ras El MA**")
st.write("07/2018 - 08/2018")
st.write(
    """
- Energetic bill optimization of the cement plant of Fez.
- Estimation of hidden energy loss throughout the production process.
- Propose solutions for recovering dissipated energy.
- Dimension and design a solar power station to cut energy consumption costs.
"""
)
st.write("\n")


# --- JOB 6
st.write('\n')
st.write("💼", "**Intern | IRESEN & LTTI Laboratories - Fez**")
st.write("06/2017 - 07/2017")
st.write(
    """
- Thermo-mechanical study of a solar boiler.
- Design a 3D model of the boiler.
- Analyze the heat transmission on the exchanger’s surfaces. 
- Determine the material mechanical characteristics required.
"""
)

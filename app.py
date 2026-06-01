import streamlit as st
import pdfplumber

st.title("Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume PDF", type="pdf")

if uploaded_file:
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    st.subheader("Resume Content")
    st.write(text)

    skills = ["Python", "Java", "SQL", "Machine Learning", "AI", "HTML", "CSS"]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Skills Found")
    st.write(found_skills)
    score = min(len(found_skills) * 10, 100)

    st.subheader("Resume Score")
    st.write(f"{score}/100")

    missing_skills = []

    for skill in skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    st.subheader("Missing Skills")
    st.write(missing_skills)
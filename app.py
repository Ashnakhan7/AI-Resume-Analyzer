import streamlit as st
import tempfile
import matplotlib.pyplot as plt

from extractor import extract_text
from extractor import extract_email
from extractor import extract_skills

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖"
)

st.title("🤖 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.read())

        path = tmp.name

    resume_text = extract_text(path)

    emails = extract_email(resume_text)

    skills = extract_skills(resume_text)

    # Email

    st.subheader("📧 Email")

    if emails:

        st.success(emails[0])

    else:

        st.error("No Email Found")

    # Skills

    st.subheader("🛠 Skills Found")

    for skill in skills:

        st.success(skill)
        
st.subheader("📊 Skills Distribution")

if skills:

    values = [1] * len(skills)

    fig, ax = plt.subplots()

    ax.pie(
        values,
        labels=skills,
        autopct='%1.0f%%'
    )

    st.pyplot(fig)

    # Read Job Description

    with open("job_description.txt", "r") as f:

        job_text = f.read().lower()

    job_skills = extract_skills(job_text)

    resume_set = set(skills)

    job_set = set(job_skills)

    matched = resume_set & job_set

    score = len(matched) / len(job_set) * 100

    # Score

    st.subheader("🎯 Resume Score")

    st.progress(int(score))

    st.write(f"### {score:.1f}% Match")

    # Candidate Rating

    st.subheader("🏆 Candidate Rating")

    if score < 40:

        st.error("Beginner 🔴")

    elif score < 70:

        st.warning("Good 🟡")

    elif score < 90:

        st.success("Strong Candidate 🟢")

    else:

        st.balloons()

        st.success("Excellent Candidate 🏆")

    # Missing Skills

    st.subheader("❌ Missing Skills")

    missing = job_set - resume_set

    if missing:

        for skill in missing:

            st.warning(skill)

    else:

        st.success("No Missing Skills")

    # AI Suggestions

    st.subheader("🤖 AI Suggestions")

    if missing:

        suggestion = ", ".join(missing)

        st.info(
            f"Your resume is good, but adding "
            f"{suggestion} can improve your chances."
        )

    else:

        st.success(
            "Your resume matches the job requirements very well!"
        )
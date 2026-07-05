import streamlit as st
import fitz

from data.course_links import COURSE_LINKS
from data.field_roles import FIELD_ROLES

from src.utils import (
    extract_skills_from_text,
    analyze_resume,
    ai_resume_feedback
)

def show_resume_tab():
    st.subheader("📄 Resume Analyzer")

    file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    if file:

        doc = fitz.open(stream=file.read(), filetype="pdf")

        text = ""

        for page in doc:
            text += page.get_text()

        skills = extract_skills_from_text(text)

        score = analyze_resume(skills)

        st.success("Resume Analysis Completed")

        # ---------------- SCORE ----------------
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("📊 Resume Score")
            st.progress(score)
            st.write(f"### {score}/100")

        with col2:
            st.subheader("🛠 Detected Skills")

            for s in skills:
                st.write(f"✔ {s}")

        # ---------------- MARKET FEEDBACK ----------------
        st.subheader("📈 Market Feedback")

        if score < 40:
            st.error("Your resume is below current market expectations")

        elif score < 70:
            st.warning("Your resume is average for current industry trends")

        else:
            st.success("Your resume matches modern industry trends")

        # ---------------- AI ANALYZER ----------------
        st.markdown("---")
        st.subheader("🤖 AI Resume Analyzer")

        roles, recommendations = ai_resume_feedback(skills)

        st.write("### 🎯 Suggested Career Roles")

        for r in roles:
            st.write(f"✔ {r}")

        st.write("### 🚀 AI Recommendations")

        for rec in recommendations:
            st.write(f"👉 {rec}")

        # ---------------- COURSE RECOMMENDATIONS ----------------
         # ---------------- COURSE RECOMMENDATIONS ----------------
        st.markdown("---")
        st.subheader("🎓 Recommended Courses Based on Your Resume")

        language = st.selectbox(
            "🌍 Choose Learning Language",
            [
                "English",
                "Tamil",
                "Hindi",
                "Malayalam",
                "Telugu",
                "Kannada"
            ],
            key="resume_language"
        )

        # AI-Based Dynamic Recommendations
        recommended_skills = []

        if "python" in skills:
            recommended_skills.extend([
                "machine learning",
                "sql",
                "tensorflow"
            ])

        if "java" in skills:
            recommended_skills.extend([
                "sql",
                "docker"
            ])

        if "html" in skills or "css" in skills:
            recommended_skills.extend([
                "javascript",
                "react",
                "nodejs"
            ])

        if "javascript" in skills:
            recommended_skills.extend([
                "react",
                "nodejs"
            ])

        if "sql" in skills:
            recommended_skills.extend([
                "power bi",
                "excel"
            ])

        if "machine learning" in skills:
            recommended_skills.extend([
                "deep learning",
                "nlp",
                "tensorflow"
            ])

        if "aws" in skills:
            recommended_skills.extend([
                "docker",
                "linux"
            ])

        # Remove duplicates
        recommended_skills = list(set(recommended_skills))

        # Display Recommended Courses
       # Display Recommended Courses
        for rec_skill in recommended_skills:

            if rec_skill not in skills:

                st.markdown(f"## 📘 {rec_skill.upper()}")

            if rec_skill in COURSE_LINKS:

                course = COURSE_LINKS[rec_skill]

            # Multilanguage Courses
            if language in course:

                youtube_link = course[language]

                st.markdown("### 🎥 YouTube Course")
                st.markdown(
                    f"[Open YouTube Course]({youtube_link})"
                )

                st.markdown("### 🏆 Certification")
                st.markdown(
                    f"[Open Certification]({course['certification']})"
                )

            # English-only Courses
            else:

                st.markdown("### 🎥 YouTube Course")
                st.markdown(
                    f"[Open YouTube Course]({course['advanced']})"
                )

                st.markdown("### 🏆 Certification")
                st.markdown(
                    f"[Open Certification]({course['certification']})"
                )

        else:

            st.info("Course database is being updated.")
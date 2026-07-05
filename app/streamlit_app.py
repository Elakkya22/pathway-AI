import streamlit as st
from home_tab import show_home_tab
from resume_tab import show_resume_tab
from skill_tab import show_skill_tab
from quiz_tab import show_quiz_tab

st.set_page_config(
    page_title="PathwayAI Pro",
    layout="wide"
)

st.title("🚀 PathwayAI Pro")
st.markdown("### Your AI-Powered Career Companion")
st.markdown("---")

tab0, tab1, tab2, tab3, tab4 = st.tabs([
    "🏠 Home",
    "📄 Resume Analysis",
    "🎯 Skill Analysis",
    "🧠 Beginner Quiz",
    "📈 Career Insights"
])
with tab0:
    show_home_tab()
with tab1:
    show_resume_tab()

with tab2:
    show_skill_tab()

with tab3:
    show_quiz_tab()
with tab4:

    st.subheader("📈 Career Insights")

    st.markdown("### 🔥 Trending Skills in 2026")

    trending_skills = [
        "Generative AI",
        "Machine Learning",
        "Power BI",
        "Cloud Computing",
        "Cybersecurity",
        "Data Analytics",
        "Docker",
        "AWS",
        "React",
        "Blockchain"
    ]

    for skill in trending_skills:
        st.write(f"✔ {skill}")

    st.markdown("---")

    st.markdown("### 💼 Popular Career Roles")

    roles = [
        "AI Engineer",
        "Data Scientist",
        "Data Analyst",
        "Frontend Developer",
        "DevOps Engineer",
        "Cloud Engineer",
        "Cybersecurity Analyst"
    ]

    for role in roles:
        st.write(f"🚀 {role}")
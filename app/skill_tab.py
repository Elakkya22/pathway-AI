import streamlit as st

from data.role_skills import ROLE_SKILLS
from data.course_links import COURSE_LINKS

from src.utils import analyze_gap
from src.roadmap import get_roadmap
from src.salary_predictor import predict_salary

def show_skill_tab():

    st.subheader("Career Skill Analysis")

    role = st.selectbox(
        "Choose Your Target Role",
        list(ROLE_SKILLS.keys())   # ✅ BEST WAY
    )

    user_input = st.text_input("Enter your skills (comma separated)")

    if user_input:

        user_skills = [s.strip().lower() for s in user_input.split(",")]

        score, matched, missing = analyze_gap(user_skills, role)

    # 🔥 SCORE
        st.subheader("Career Readiness Score")
        st.progress(int(score))
        st.write(f"### {score:.2f}% Match")

    # 🔥 LEVEL
        if score < 30:
            st.error("Beginner Level")
        elif score < 60:
             st.warning("Intermediate Level")
        elif score < 80:
            st.info("Job Ready")
        else:
            st.success("Advanced Level")

    # 🔥 MATCHED SKILLS
        st.subheader("Matched Skills")

        for m in matched:
            st.write(f"✔ {m}")

    # 🔥 MISSING SKILLS
        st.subheader("Missing Skills")

        for m in missing:
            st.write(f"❌ {m}")
            # ---------------- ROADMAP ----------------

        roadmap = get_roadmap(role)

        st.markdown("---")
        st.subheader("🛣 Career Roadmap")

        for step in roadmap:
            st.write(f"✔ {step}")
            # ---------------- SALARY ----------------

        salary = predict_salary(role)

        st.markdown("---")
        st.subheader("💰 Expected Salary")

        st.success(salary)
    # 🔥 LEARNING PATH
       
        st.markdown("---")
        st.subheader("🎓 Recommended Courses")

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
            key="skill_language"
        )

        for skill in missing:

            st.markdown(f"## 📘 {skill.upper()}")

            if skill in COURSE_LINKS:

                course = COURSE_LINKS[skill]

                youtube_link = course[language]

                st.markdown("### 🎥 YouTube Course")
                st.markdown(
                f"[Open YouTube Course]({youtube_link})"
                )

                st.markdown("### 🏆 Certification")
                st.markdown(
                f"[Open Certification]({course['certification']})"
                )

            else:
                st.write("No course available yet.")
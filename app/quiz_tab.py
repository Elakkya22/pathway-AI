import streamlit as st
import random

from data.quiz_data import QUIZ_DATA
from data.course_links import COURSE_LINKS

def show_quiz_tab():
    st.subheader("🧠 Beginner Friendly Quiz")

    score = 0

    # ---------------- QUIZ QUESTIONS ----------------

    for q in QUIZ_DATA:

        st.markdown("---")

        st.write(f"### {q['question']}")

        options = q["options"].copy()

        random.shuffle(options)

        user_answer = st.radio(
            "Choose your answer",
            options,
            key=q["question"]
        )

        if user_answer == q["answer"]:
            score += 1

    st.markdown("---")

    # ---------------- SKILL DISCOVERY ----------------

    skills = []

    # PROGRAMMING
    knows_programming = st.radio(
        "Do you know programming?",
        ["Yes", "No"]
    )

    if knows_programming == "Yes":

        lang = st.selectbox(
            "Which language do you know?",
            ["Python", "Java", "C++", "JavaScript"]
        )

        skills.append(lang.lower())

        level = st.slider(
            "Programming Confidence",
            1,
            10
        )

    # WEB DEVELOPMENT
    web = st.radio(
        "Do you know Web Development?",
        ["Yes", "No"]
    )

    if web == "Yes":

        web_skill = st.multiselect(
            "Which web technologies?",
            ["HTML", "CSS", "JavaScript", "React"]
        )

        for s in web_skill:
            skills.append(s.lower())

    # DATABASES
    db = st.radio(
        "Do you know databases?",
        ["Yes", "No"]
    )

    if db == "Yes":

        db_skill = st.selectbox(
            "Choose database skill",
            ["SQL", "MongoDB", "PostgreSQL"]
        )

        skills.append(db_skill.lower())

    # AI / ML
    ai = st.radio(
        "Interested in AI / Machine Learning?",
        ["Yes", "No"]
    )

    if ai == "Yes":

        ai_skill = st.multiselect(
            "Which AI topics?",
            [
                "Machine Learning",
                "Deep Learning",
                "NLP"
            ]
        )

        for s in ai_skill:
            skills.append(s.lower())

    # CLOUD / DEVOPS
    cloud = st.radio(
        "Do you know Cloud or DevOps?",
        ["Yes", "No"]
    )

    if cloud == "Yes":

        cloud_skill = st.multiselect(
            "Choose technologies",
            ["AWS", "Docker", "Kubernetes"]
        )

        for s in cloud_skill:
            skills.append(s.lower())

    # ---------------- FINAL OUTPUT ----------------

    if st.button("Generate My Skills"):

        st.success("Skills Generated Successfully")

        st.subheader("🎯 Your Skills")

        for s in skills:
            st.write(f"✔ {s}")

        st.subheader("📊 Quiz Score")

        st.progress(score / len(QUIZ_DATA))

        st.write(
            f"### {score} / {len(QUIZ_DATA)} Correct"
        )

        # ---------------- COURSE RECOMMENDATIONS ----------------

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
            key="quiz_language"
        )

        for skill in skills:

            if skill in COURSE_LINKS:

                st.markdown(f"## 📘 {skill.upper()}")

                course = COURSE_LINKS[skill]

                # 🌍 MULTILANGUAGE COURSES
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

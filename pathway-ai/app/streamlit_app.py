import streamlit as st
import fitz  # PyMuPDF
ROLE_SKILLS = {

    "Data Scientist": ["python", "machine learning", "sql", "statistics"],
    "Data Analyst": ["excel", "sql", "python"],
    "Machine Learning Engineer": ["python", "machine learning", "tensorflow"],
    "AI Engineer": ["python", "deep learning", "nlp"],
    "Web Developer": ["html", "css", "javascript", "react"],
    "Frontend Developer": ["html", "css", "javascript", "react"],
    "Backend Developer": ["python", "java", "api"],
    "Full Stack Developer": ["html", "css", "javascript", "nodejs"],
    "Software Engineer": ["python", "java", "algorithms"],
    "Mobile App Developer": ["flutter", "android"],
    "DevOps Engineer": ["linux", "docker", "ci/cd"],
    "Cloud Engineer": ["aws", "azure", "cloud"],
    "Site Reliability Engineer": ["linux", "monitoring"],
    "Cybersecurity Analyst": ["networking", "security"],
    "Ethical Hacker": ["penetration testing", "security"],
    "Data Engineer": ["python", "sql", "etl"],
    "AI Product Manager": ["ai", "business"],
    "Blockchain Developer": ["blockchain", "web3"]
}
COURSES = {
    "python": "Python for Beginners – YouTube / Coursera",
    "machine learning": "Machine Learning by Andrew Ng – Coursera",
    "sql": "SQL Bootcamp – Udemy",
    "html": "HTML Crash Course – YouTube",
    "css": "CSS Full Course – YouTube",
    "javascript": "JavaScript Course – Udemy",
    "react": "React JS Course – YouTube",
    "deep learning": "Deep Learning Specialization – Coursera",
    "nlp": "NLP Course – Coursera",
    "tensorflow": "TensorFlow Developer Course",
    "pandas": "Data Analysis with Pandas",
    "numpy": "NumPy Tutorial",
    "excel": "Excel for Data Analysis",
    "power bi": "Power BI Full Course",
    "docker": "Docker for Beginners",
    "aws": "AWS Cloud Practitioner",
    "linux": "Linux Basics Course"
}
st.set_page_config(page_title="PathwayAI Pro", layout="wide")

st.title("🚀 PathwayAI Pro")
st.markdown("### Your AI-Powered Career Companion")
st.markdown("---")

def analyze_gap(user_skills, role):
       
    required = ROLE_SKILLS.get(role, [])

    matched = [s for s in required if s in user_skills]
    missing = [s for s in required if s not in user_skills]

    score = (len(matched) / len(required)) * 100 if required else 0

    return score, matched, missing
# ---------------- SKILL DETECTOR ----------------
def extract_skills_from_text(text):
    skills_db = [
        "python", "machine learning", "sql", "data analysis",
        "html", "css", "javascript", "react",
        "tensorflow", "pytorch", "nlp", "deep learning"
    ]

    found = []

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return list(set(found))


# ---------------- RESUME SCORE ----------------
def analyze_resume(skills):
    score = len(skills) * 10

    if score > 100:
        score = 100

    return score


# ---------------- UI ----------------
tab1, tab2, tab3 = st.tabs(["📄 Resume Analysis", "🎯 Skill Analysis", "🧠 Beginner Quiz"])

# ---------------- RESUME TAB ----------------
with tab1:
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

        # Layout columns
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("📊 Resume Score")
            st.progress(score)
            st.write(f"### {score}/100")

        with col2:
            st.subheader("Detected Skills")
            for s in skills:
                st.write(f"✔ {s}")

        # Feedback
        st.subheader("Market Feedback")

        if score < 40:
            st.error("Not aligned with market")
        elif score < 70:
            st.warning("Average resume")
        else:
            st.success("Strong resume")

        # Suggestions
        st.subheader("Improve Your Resume")

        suggestions = ["machine learning", "sql", "react", "cloud"]

        for s in suggestions:
            if s not in skills:
                st.write(f"Add {s}")

# ---------------- SKILL TAB ----------------
# ---------------- SKILL TAB ----------------
with tab2:
    st.subheader("Career Skill Analysis")

    role = st.selectbox(
        "Choose Your Target Role",
        list(ROLE_SKILLS.keys())   # ✅ BEST WAY
    )

    user_input = st.text_input("Enter your skills (comma separated)")

    if user_input:
        user_skills = [s.strip().lower() for s in user_input.split(",")]

        score, matched, missing = analyze_gap(user_skills, role)

        # 🔥 SCORE SECTION
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

        st.markdown("---")

        # 🔥 SIDE-BY-SIDE DISPLAY
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Your Strengths")
            for m in matched:
                st.write(f"✔ {m}")

        with col2:
            st.subheader("Skill Gaps")
            for m in missing:
                st.write(f"❌ {m}")

        # 🔥 LEARNING PATH
        st.markdown("---")
        st.subheader("Recommended Learning Path")

        for m in missing:
            st.write(f"Learn: {m}")
            st.markdown("---")
st.subheader("🎓 Recommended Courses")

for m in missing:
    course = COURSES.get(m, "Search on YouTube")
    st.write(f"👉 {m} → {course}")
            # ---------------- GAP FUNCTION (MOVE THIS ABOVE TABS) ----------------

# ---------------- QUIZ TAB ----------------
with tab3:
    st.subheader("Beginner Friendly Quiz")

    skills = []

    # Q1
    knows_programming = st.radio("Do you know programming?", ["Yes", "No"])

    if knows_programming == "Yes":

        lang = st.selectbox(
            "Which programming language do you know?",
            ["Python", "Java", "C++", "JavaScript"]
        )

        level = st.slider("Your confidence level?", 1, 5)

        if lang == "Python":
            skills.append("python")
        elif lang == "JavaScript":
            skills.append("javascript")
        elif lang == "Java":
            skills.append("java")

        if level >= 3:
            skills.append("problem solving")

    # Q2
    knows_web = st.radio("Do you know web development?", ["Yes", "No"])

    if knows_web == "Yes":
        skills.extend(["html", "css", "javascript"])

        framework = st.selectbox(
            "Do you know any framework?",
            ["None", "React", "Angular"]
        )

        if framework == "React":
            skills.append("react")

    # Q3
    knows_data = st.radio("Are you interested in Data / AI?", ["Yes", "No"])

    if knows_data == "Yes":
        skills.append("machine learning")

        exp = st.selectbox(
            "Have you worked with data?",
            ["No", "Basic Excel", "Python Data Analysis"]
        )

        if exp == "Basic Excel":
            skills.append("excel")
        elif exp == "Python Data Analysis":
            skills.extend(["pandas", "numpy"])

    # FINAL BUTTON
    if st.button("Generate My Skills"):

        skills = list(set(skills))

        st.subheader("Your Generated Skills")

        if skills:
            for s in skills:
                st.write(f"✔ {s}")
        else:
            st.warning("No skills detected. Try answering Yes to some questions.")

        # Optional role mapping
        st.subheader("Suggested Career Path")

        if "machine learning" in skills:
            st.success("Recommended Role: Data Scientist / AI Engineer")
        elif "html" in skills:
            st.success("Recommended Role: Web Developer")
        elif "python" in skills:
            st.success("Recommended Role: Software Engineer")
        else:
            st.info("Explore different domains to find your interest")
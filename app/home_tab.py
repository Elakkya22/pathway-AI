import streamlit as st

def show_home_tab():

    st.title("🚀 PATHWAY-AI")

    st.write(
        "AI-Powered Career Guidance Platform"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Roles", "15+")

    with col2:
        st.metric("Skills", "30+")

    with col3:
        st.metric("Courses", "50+")

    st.markdown("---")

    st.subheader("Features")

    st.write("📄 Resume Analyzer")
    st.write("🎯 Skill Gap Analysis")
    st.write("🧠 Beginner Quiz")
    st.write("🛣 Career Roadmap")
    st.write("💰 Salary Prediction")
    st.write("🔥 Trending Skills")
    st.write("🌍 Multilingual Learning")
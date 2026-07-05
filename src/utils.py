from data.role_skills import ROLE_SKILLS
from data.field_roles import FIELD_ROLES


def analyze_gap(user_skills, role):

    required = ROLE_SKILLS.get(role, [])

    matched = [
        s for s in required
        if s in user_skills
    ]

    missing = [
        s for s in required
        if s not in user_skills
    ]

    score = (
        len(matched) / len(required)
    ) * 100 if required else 0

    return score, matched, missing


def extract_skills_from_text(text):

    skills_db = [
        "python",
        "machine learning",
        "sql",
        "html",
        "css",
        "javascript",
        "react",
        "tensorflow",
        "deep learning",
        "nlp",
        "aws",
        "docker",
        "power bi"
    ]

    found = []

    text = text.lower()

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return list(set(found))


def analyze_resume(skills):

    score = len(skills) * 10

    if score > 100:
        score = 100

    return score


def ai_resume_feedback(skills):

    suggested_roles = []

    recommendations = []

    # Find roles from skills
    for skill in skills:

        if skill in FIELD_ROLES:

            suggested_roles.append(
                FIELD_ROLES[skill]
            )

    suggested_roles = list(set(suggested_roles))

    # Role-based recommendations

    if "AI Engineer" in suggested_roles:

        if "machine learning" not in skills:
            recommendations.append("machine learning")

        if "deep learning" not in skills:
            recommendations.append("deep learning")

        if "tensorflow" not in skills:
            recommendations.append("tensorflow")

    if "Data Analyst" in suggested_roles:

        if "excel" not in skills:
            recommendations.append("excel")

        if "power bi" not in skills:
            recommendations.append("power bi")

        if "statistics" not in skills:
            recommendations.append("statistics")

    if "Frontend Developer" in suggested_roles:

        if "react" not in skills:
            recommendations.append("react")

        if "javascript" not in skills:
            recommendations.append("javascript")

    if "DevOps Engineer" in suggested_roles:

        if "docker" not in skills:
            recommendations.append("docker")

        if "aws" not in skills:
            recommendations.append("aws")

    recommendations = list(set(recommendations))

    return suggested_roles, recommendations
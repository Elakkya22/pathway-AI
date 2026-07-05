def analyze_gap(user_skills):
    # Define target role skills (for now static)
    required_skills = [
        "python",
        "machine learning",
        "sql",
        "statistics",
        "data visualization"
    ]

    matched = []
    missing = []

    for skill in required_skills:
        if skill in user_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    match_score = (len(matched) / len(required_skills)) * 100

    return match_score, matched, missing
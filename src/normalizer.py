def normalize_skills(skills):
    normalized = []

    for skill in skills:
        skill = skill.lower().strip()

        # Basic synonym handling
        if skill in ["python3", "py"]:
            skill = "python"
        elif skill in ["ml"]:
            skill = "machine learning"
        elif skill in ["ai"]:
            skill = "artificial intelligence"

        normalized.append(skill)

    # Remove duplicates
    normalized = list(set(normalized))

    return normalized
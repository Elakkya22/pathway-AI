def get_user_skills(input_text):
    skills = input_text.lower().split(",")
    skills = [skill.strip() for skill in skills]
    return skills
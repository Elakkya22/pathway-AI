def predict_salary(role):

    salaries = {

        "AI Engineer": "8 - 15 LPA",

        "Data Analyst": "4 - 10 LPA",

        "Frontend Developer": "4 - 8 LPA",

        "DevOps Engineer": "6 - 12 LPA",

        "Cloud Engineer": "6 - 14 LPA"
    }

    return salaries.get(
        role,
        "Salary data unavailable"
    )
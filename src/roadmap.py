def get_roadmap(role):

    roadmaps = {

        "AI Engineer": [
            "Learn Python",
            "Learn Machine Learning",
            "Learn Deep Learning",
            "Learn TensorFlow",
            "Build AI Projects"
        ],

        "Machine Learning Engineer": [
            "Learn Python",
            "Learn Statistics",
            "Learn Machine Learning",
            "Learn Scikit-Learn",
            "Build ML Projects"
        ],

        "Data Analyst": [
            "Learn Excel",
            "Learn SQL",
            "Learn Power BI",
            "Learn Statistics",
            "Build Dashboard Projects"
        ],

        "Business Analyst": [
            "Learn Excel",
            "Learn SQL",
            "Learn Power BI",
            "Learn Business Analytics",
            "Create Reports & Dashboards"
        ],

        "Frontend Developer": [
            "Learn HTML",
            "Learn CSS",
            "Learn JavaScript",
            "Learn React",
            "Build Web Applications"
        ],

        "Web Developer": [
            "Learn HTML",
            "Learn CSS",
            "Learn JavaScript",
            "Learn React",
            "Build Full Stack Projects"
        ],

        "Software Engineer": [
            "Master Java",
            "Learn DSA",
            "Learn OOP",
            "Build Applications",
            "Practice Coding Problems"
        ],

        "DevOps Engineer": [
            "Learn Linux",
            "Learn Docker",
            "Learn AWS",
            "Learn CI/CD",
            "Deploy Projects"
        ],

        "Cloud Engineer": [
            "Learn AWS",
            "Learn Linux",
            "Learn Docker",
            "Learn Cloud Security",
            "Deploy Cloud Projects"
        ],

        "Cybersecurity Analyst": [
            "Learn Networking",
            "Learn Linux",
            "Learn Security Fundamentals",
            "Learn Penetration Testing",
            "Practice Security Labs"
        ]
    }

    return roadmaps.get(role, ["No roadmap available"])
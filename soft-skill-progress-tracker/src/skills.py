import json
from datetime import date

FILE = "data/skills.json"

def add_log():
    skill = input("Skill Name: ")
    description = input("Description: ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")
    lesson = input("Lesson Learned: ")

    log = {
        "skill": skill,
        "description": description,
        "date": str(date.today()),
        "difficulty": difficulty,
        "lesson": lesson
    }

    try:
        data = json.load(open(FILE))
    except:
        data = []

    data.append(log)
    json.dump(data, open(FILE, "w"), indent=4)

def view_logs():
    try:
        data = json.load(open(FILE))
        for log in data:
            print(log)
    except:
        print("No logs found")

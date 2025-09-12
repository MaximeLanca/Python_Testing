import json

def save_clubs(clubs, path="clubs.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"clubs": clubs}, f, indent=2, ensure_ascii=False)

def save_competitions(competitions, path="competitions.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"competitions": competitions}, f, indent=2, ensure_ascii=False)
import json


def save_clubs(clubs, path="clubs.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"clubs": clubs}, f, indent=2, ensure_ascii=False)


def save_competitions(competitions, path="competitions.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"competitions": competitions}, f, indent=2, ensure_ascii=False)


def load_clubs():
    with open("clubs.json") as c:
        clubs_list = json.load(c)["clubs"]
        return clubs_list


def load_competitions():
    with open("competitions.json") as comps:
        competitions_list = json.load(comps)["competitions"]
        return competitions_list

def save_booking(booking, path='bookings.json'):
    bookings = load_booking(path)
    bookings.append(booking)
    with open(path,'w', encoding='utf-8') as f:
        json.dump({'bookings' : bookings}, f, indent=2, ensure_ascii=False)

def load_booking(path='bookings.json'):
    with open(path,"r", encoding="utf-8") as b:
            data = json.load(b)
            return data.get("bookings", [])
   
        

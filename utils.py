from datetime import datetime

def check_competition_date(date_str, format="%Y-%m-%d %H:%M:%S"):
    competition_date = datetime.strptime(date_str, format)
    return competition_date > datetime.now()

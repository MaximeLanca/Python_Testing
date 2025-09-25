from datetime import datetime
from data import load_booking


def check_competition_date(date_str):
    format = "%Y-%m-%d %H:%M:%S"
    competition_date = datetime.strptime(date_str, format)
    return competition_date > datetime.now()


def get_places_purchased(club,competition):
    bookings_list = load_booking()
    places_purchased = 0
    for booking in bookings_list:
        if (booking['club'] == club['name']) and (booking['competition'] == competition['name']):
            places_purchased =+ int(booking['places'])
    return places_purchased


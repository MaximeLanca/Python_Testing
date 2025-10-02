from datetime import datetime
from data import load_booking
from flask import Blueprint

filters_bp = Blueprint("filters", __name__)

@filters_bp.app_template_filter("check_competition_date")
def check_competition_date(date_str):
    format = "%Y-%m-%d %H:%M:%S"
    competition_date = datetime.strptime(date_str, format)
    return competition_date > datetime.now()


def get_purchased_places(club,competition):
    bookings_list = load_booking()
    places_purchased = 0
    for booking in bookings_list:
        if (booking['club'] == club) and (booking['competition'] == competition):
            places_purchased += int(booking['places'])
    return places_purchased


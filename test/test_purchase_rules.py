from utils import get_purchased_places
from unittest.mock import patch
from unittest.mock import patch
import json, server

def test_purchase_places_in_competition(client, bookings_path):

    with patch.object(server, "clubs", [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "25"}
        ], create=True), \
         patch.object(server, "competitions", [
            {"name": "Spring Festival", "date": "2027-10-10 09:00:00", "numberOfPlaces": "13"}
        ], create=True):

        resp = client.post("/purchase_places", data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "12", 
        }, follow_redirects=True)
        assert resp.status_code == 200

        bookings = json.loads(bookings_path.read_text(encoding="utf-8"))["bookings"]
        assert bookings[0]['competition'] == 'Spring Festival'
        assert bookings[0]['club'] == 'Simply Lift'
        assert bookings[0]['places'] == '12'



@patch.object(server, "clubs", [
    {"name": "Simply Lift", "email": "john@simplylift.co", "points": "25"}
])
@patch.object(server, "competitions", [
    {"name": "Spring Festival", "date": "2027-10-10 09:00:00", "numberOfPlaces": "10"}
])
@patch("server.save_booking", lambda *a, **k: None)
@patch("server.save_clubs", lambda *a, **k: None)
@patch("server.save_competitions", lambda *a, **k: None)
def test_purchase_places_more_than_available():
    client = server.app.test_client()

    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "12",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert int(server.competitions[0]["numberOfPlaces"]) == 10


@patch.object(server, "clubs", [
    {"name": "Simply Lift", "email": "john@simplylift.co", "points": "25"}
])
@patch.object(server, "competitions", [
    {"name": "Spring Festival", "date": "2023-08-10 09:00:00", "numberOfPlaces": "10"}
])
@patch("server.save_booking", lambda *a, **k: None)
@patch("server.save_clubs", lambda *a, **k: None)
@patch("server.save_competitions", lambda *a, **k: None)
def test_purchase_places_in_finished_competition():
    client = server.app.test_client()

    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "2",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert int(server.competitions[0]["numberOfPlaces"]) == 10



@patch.object(server, "clubs", [
    {"name": "Simply Lift", "email": "john@simplylift.co", "points": "25"}
])
@patch.object(server, "competitions", [
    {"name": "Spring Festival", "date": "2027-10-10 09:00:00", "numberOfPlaces": "20"}
])
@patch("server.save_booking", lambda *a, **k: None)
@patch("server.save_clubs", lambda *a, **k: None)
@patch("server.save_competitions", lambda *a, **k: None)
def test_purchase_twelve_places_limit_enforced():

    client = server.app.test_client()
    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "20",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert int(server.competitions[0]["numberOfPlaces"]) == 20


def test_purchase_twelve_places_in_multiple_requests():

    with patch.object(server, "clubs", [
    {"name": "Simply Lift", "email": "john@simplylift.co", "points": "25"}
    ], create=True), \
     patch.object(server, "competitions", [
    {"name": "Spring Festival", "date": "2027-10-10 09:00:00", "numberOfPlaces": "25"}
    ], create=True):
    
        client = server.app.test_client()
        resp1 = client.post(
            "/purchase_places",
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": "11",
            },
            follow_redirects=True,
        )
        assert resp1.status_code == 200
        assert get_purchased_places("Simply Lift","Spring Festival") == 11

        resp2 = client.post(
            "/purchase_places",
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": "1",
            },
            follow_redirects=True,
        )
        assert resp2.status_code == 200
        assert get_purchased_places("Simply Lift","Spring Festival") == 12

        resp3 = client.post(
            "/purchase_places",
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": "1",
            },
            follow_redirects=True,
        )
        assert resp3.status_code == 200
        assert get_purchased_places("Simply Lift","Spring Festival") == 12

from utils import get_purchased_places

def test_purchase_places_parametrized(client, competition_line_up_twenty_five_places):
    competition = competition_line_up_twenty_five_places
    before = int(competition[0]["numberOfPlaces"])
    assert before == 25
    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "13",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    after = int(competition[0]["numberOfPlaces"])
    assert after == 12



def test_purchase_places_more_than_available(client, competition_line_up_ten_places):
    competition = competition_line_up_ten_places
    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "12",
        },
        follow_redirects=True,
    )

    after = int(competition[0]["numberOfPlaces"])
    assert after == 10


def test_purcharse_places_with_ten_points(client, club_with_ten_points):
    club = club_with_ten_points
    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "12",
        },
        follow_redirects=True,
    )

    after = int(club[0]["points"])
    assert after == 10


def test_purchase_places_in_finished_competition(client, finished_competition):
    competition = finished_competition
    response = client.post("/purchase_places", data ={
        "competition":"Spring Festival",
        "club" : "Simply Lift",
        "places" : "2",
        },
        follow_redirects=True)
    
    after = int(competition[0]["numberOfPlaces"])
    assert after == 10


def test_purchase_twelve_places(client, limit_purchase_twelve_places_in_different_section):
    places_purchased = limit_purchase_twelve_places_in_different_section
    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "20",
    },
        follow_redirects=True,
    )
    after = places_purchased 
    assert after == 12

def test_purchase_twelve_places(client, limit_purchase_twelve_places_in_different_section):
    places_purchased = limit_purchase_twelve_places_in_different_section
    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "11",
    },
        follow_redirects=True,
    )
    assert get_purchased_places({"name":"Simply Lift"},{"name":"Spring Festival"}) == 11

    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "1",
    },
        follow_redirects=True,
    )
    assert get_purchased_places({"name":"Simply Lift"},{"name":"Spring Festival"}) == 12

    response = client.post(
        "/purchase_places",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "1",
    },
        follow_redirects=True,
    )
    assert get_purchased_places({"name":"Simply Lift"},{"name":"Spring Festival"}) == 12



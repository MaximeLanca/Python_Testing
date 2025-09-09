import pytest


@pytest.mark.parametrize("places,expected_remaining", [(12, 13),(13, 25)])
def test_purchase_places_parametrized(client, competition_line_up_twenty_five_places, places, expected_remaining):
    competition = competition_line_up_twenty_five_places
    before = int(competition[0]["numberOfPlaces"])
    assert before == 25
    response = client.post("/purchasePlaces", data ={
        "competition":"Spring Festival",
        "club" : "Simply Lift",
        "places" : str(places),
        },
        follow_redirects=True)
    
    assert response.status_code == 200
    after = int(competition[0]["numberOfPlaces"])
    assert after == expected_remaining 

def test_purchase_places_more_than_available(client, competition_line_up_ten_places):
    competition = competition_line_up_ten_places
    response = client.post("/purchasePlaces", data ={
        "competition":"Spring Festival",
        "club" : "Simply Lift",
        "places" : "12",
        },
        follow_redirects=True)
    
    after = int(competition[0]["numberOfPlaces"])
    assert after == 10





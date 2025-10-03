import pytest
import server
import data


# @pytest.fixture(autouse=True)
# def patch_reload(monkeypatch):
#     def fake_reload():
#         server.clubs = data.load_clubs()
#         server.competitions = data.load_competitions()
#     monkeypatch.setattr(server, "reload_data", fake_reload, raising=True)

@pytest.fixture
def app():
    """Fixture requise par pytest-flask : retourne l'app Flask."""
    server.app.config.update(TESTING=True, SECRET_KEY="test")
    return server.app


@pytest.fixture
def client():
    return server.app.test_client()


@pytest.fixture
def user_context():
    data = {
        "name": "Simply Lift",
        "email": "john@simplylift.co",
    }
    return data


@pytest.fixture
def competition_line_up_twenty_five_places(monkeypatch):
    monkeypatch.setattr(
        server,
        "load_competitions",
        lambda: [
            {
                "name": "Spring Festival",
                "date": "2027-10-10 09:00:00",
                "numberOfPlaces": "25",
            }
        ],
    )
    return [
            {
                "name": "Spring Festival",
                "date": "2027-10-10 09:00:00",
                "numberOfPlaces": "25",
            }
        ]


@pytest.fixture
def competition_line_up_ten_places(monkeypatch):
    monkeypatch.setattr(
        data,
        "load_competitions",
        lambda: [
            {
                "name": "Spring Festival",
                "date": "2027-10-10 09:00:00",
                "numberOfPlaces": "10",
            }
        ],
    )
    server.reload_data()
    return server.competitions


@pytest.fixture
def finished_competition(monkeypatch):
    monkeypatch.setattr(
        data,
        "load_competitions",
        lambda: [
            {
                "name": "Spring Festival",
                "date": "2025-08-10 09:00:00",
                "numberOfPlaces": "10",
            }
        ],
    )
    server.reload_data()
    return server.competitions

@pytest.fixture
def club_with_twenty_five_points(monkeypatch):
    monkeypatch.setattr(
        data,
        "load_clubs",
        lambda: [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "25"}
        ],
    )
    return [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "25"}
        ],

@pytest.fixture
def club_with_ten_points(monkeypatch):
    monkeypatch.setattr(
        data,
        "load_clubs",
        lambda: [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "10"}
        ],
    )
    return [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "10"}
        ]


@pytest.fixture
def clubs_simply_lift(monkeypatch):
    monkeypatch.setattr(
        data,
        "load_clubs",
        lambda: [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}
        ],
    )
    return [
            {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}
        ]



@pytest.fixture(autouse=True)
def no_backup(monkeypatch):
    monkeypatch.setattr("data.save_clubs", lambda clubs, path="clubs.json": None, raising=True)
    monkeypatch.setattr("data.save_competitions", lambda comps, path="competitions.json": None, raising=True)
    monkeypatch.setattr("data.save_booking", lambda bookings, path="bookings.json": None, raising=True)
  
  
@pytest.fixture
def limit_purchase_twelve_places_in_different_section(monkeypatch):
    monkeypatch.setattr("utils.get_purchased_places",lambda path="bookings.json":"bookings_for_tests.json",raising=True)
    monkeypatch.setattr("data.save_booking", lambda bookings, path="bookings.json":None,raising=True)
    monkeypatch.setattr("data.save_competitions", lambda comps, path="competitions.json": None, raising=True)
    
